import py7zr
from ftplib import FTP
from io import BytesIO
import os
import pandas as pd
import s3fs

def send_to_s3(df, date, file_name):
    fs = s3fs.S3FileSystem(key='key',
    secret='acess')

    df.to_parquet('s3://{}/{}/{}'.format('a3datahackaton', date, f'{file_name}.parquet'), filesystem=fs)

    
def exclude_empty_columns(df):
    for col in df.columns:
        try:
            if any(df[col].str.contains('{ñ class}')):
                df[col] = df[col].apply(lambda x: ''.join(x.split()))
                if df[col].nunique() == 1:
                    del df[col]
        except:
            print(col)

def keep_connection_alive(date):
    ftp = FTP('189.9.32.26')
    ftp.login()
    ftp.cwd(f'pdet/microdados/RAIS/{date}')

            
def retrive_files():
    dates = [str(date) for date in range(2010,2020)]
    ftp = FTP('189.9.32.26')
    ftp.login()
    for date in dates:
        ftp.cwd("~")
        ftp.cwd(f'pdet/microdados/RAIS/{date}')
        list_of_files = ftp.nlst()
        for file in list_of_files:
            print(file)
            download_file = BytesIO()
            ftp.retrbinary(f'RETR {file}', download_file.write)
            download_file.seek(0)
            archive = py7zr.SevenZipFile(download_file, mode='r')
            archive.extractall(path=os.getcwd())
            archive.close()
            file_name = file.split('.')[0]
            df = pd.read_csv(file_name + '.txt', sep = ';', encoding='latin-1', low_memory=False, dtype = 'unicode')
            exclude_empty_columns(df)
#             send_to_s3(df, date, file_name)
            os.remove(file_name + '.txt') 
            keep_connection_alive(date)

            
if __name__ == '__main__':
    retrive_files()
    