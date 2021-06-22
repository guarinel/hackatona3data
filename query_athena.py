import time
import boto3
import pandas as pd
import io
from querys_sql import *

class QueryAthena:

    def __init__(self, query, database):
        self.database = database
        self.folder = 'final_querys'
        self.bucket = 'a3datahackaton'
        self.region_name = 'sa-east-1'
        self.aws_access_key_id = "acess"
        self.aws_secret_access_key = "key"
        self.query = query

    def load_conf(self, q):
        try:
            self.client = boto3.client('athena', 
                              region_name = self.region_name, 
                              aws_access_key_id = self.aws_access_key_id,
                              aws_secret_access_key= self.aws_secret_access_key)
            response = self.client.start_query_execution(
                QueryString = q,
                    QueryExecutionContext={
                    'Database': self.database
                    },
                    ResultConfiguration={
                    'OutputLocation': self.s3_output,
                    }
            )
            self.filename = response['QueryExecutionId']
            print('Execution ID: ' + response['QueryExecutionId'])

        except Exception as e:
            print(e)
        return response                

    def run_query(self):
        dict_of_dfs = {}
        queries = self.query
        for q in queries:
            self.s3_output =  's3://' + self.bucket + '/' + self.folder + q[2]
            res = self.load_conf(q[0])
            try:              
                query_status = None
                while query_status == 'QUEUED' or query_status == 'RUNNING' or query_status is None:
                    query_status = self.client.get_query_execution(QueryExecutionId=res["QueryExecutionId"])['QueryExecution']['Status']['State']
                    print(query_status)
                    if query_status == 'FAILED' or query_status == 'CANCELLED':
                        raise Exception('Athena query with the string "{}" failed or was cancelled'.format(self.query))
                    time.sleep(15)
                print('Query "{}" finished.'.format(q[2]))

                if q[1]:
                    dict_of_dfs[q[2]] = self.obtain_data(q[2])
            except Exception as e:
                print(e)               
        return dict_of_dfs
    
    def obtain_data(self, path):
        try:
            self.resource = boto3.resource('s3', 
                                  region_name = self.region_name, 
                                  aws_access_key_id = self.aws_access_key_id,
                                  aws_secret_access_key= self.aws_secret_access_key)

            response = self.resource \
            .Bucket(self.bucket) \
            .Object(key= self.folder + path + "/" + self.filename  + '.csv') \
            .get()

            return pd.read_csv(io.BytesIO(response['Body'].read()), encoding='utf8')   
        except Exception as e:
            print(e)  

def concat_df_years(dataframe):
    dict_first_question = {}
    dict_second_question = {}
    dict_third_question = {}
    dict_forth_question = {}

    for key in dataframe:
        dict_first_question[key] = dataframe[key]['/answer_1']
        dict_second_question[key] = dataframe[key]['/answer_2']
        dict_third_question[key] = dataframe[key]['/answer_3']
        dict_forth_question[key] = dataframe[key]['/answer_4']
        
        
    pd.concat(dict_first_question).reset_index()[['sexo', 'regiao', '_col2', 'ano']].to_csv('answer_1.csv', index = False)
    pd.concat(dict_second_question).reset_index()[['escolaridade', 'regiao', '_col1', 'ano']].to_csv('answer_2.csv', index = False)
    pd.concat(dict_third_question).reset_index()[['soma_admissao', 'soma_demissao', 'cnae_d','qnt_trabalhadores', 'ano', 'setor']].to_csv('answer_3.csv', index = False)
    pd.concat(dict_forth_question).reset_index()[['sum_less_than_forty', 'cnae_d', 'ano']].to_csv('answer_4.csv', index = False)



if __name__ == "__main__":       
    dates = [str(date) for date in range(2010,2020)]
    dataframe = {}
    dataframe_q5 = {}
    for date in dates:
        """
        Construção da lista query:
        Carrega query SQL do arquivo, primeiro parametro do format é o nome da view;
        Segundo parametro é o ano;
        Terceiro parametro é a table original que vem o FROM;
        False indica se é para baixar o resultado .csv do s3;
        O argumento último é o path caso tenha q salvar 

        As 3 primeiras querys são as views, e as últimas 5 são querys simples, 
        completamente agrupadas para responder as perguntas do hackaton.
        """

        query = [
                (base_query_1_layout.format(f"base_query_{date}",date, date), False, ""),
                 (second_query_1_layout.format(f"second_query{date}", f"base_query_{date}"), False, ""),
                 (third_query_2_layout.format(f"third_query{date}", f"base_query_{date}"), False, ""),   
                 
                 (query_q1.format(f"second_query{date}"), True, '/answer_1'),
                 (query_q2.format(f"second_query{date}"), True, '/answer_2'),
                 (query_q3.format(f"third_query{date}"), True, '/answer_3'),
                 (query_q4.format(f"third_query{date}"), True, '/answer_4')]      
        qa = QueryAthena(query=query, database='a3datahackaton')
        dataframe[date] = qa.run_query()
        
    concat_df_years(dataframe)
    
    for date in ['2018', '2019']:
        query = [(query_q5.format(date, date), True, '/answer_5')]
        qa = QueryAthena(query=query, database='a3datahackaton')
        dataframe_q5[date] = qa.run_query()

    pd.concat([dataframe_q5['2018']['/answer_5'],dataframe_q5['2019']['/answer_5']]).to_csv('answer_5.csv', index = False)

        
            
