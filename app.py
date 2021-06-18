import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_train():
    train = pd.read_csv('https://www.dropbox.com/s/7vexlzohz7j3qem/train.csv?raw=1', index_col=0)
    return train


# Fazendo cache dos dados para acelerar as próximas pesquisas.
@st.cache(allow_output_mutation=True)
def load_train():
    dict_of_df = {}
    links = ['https://www.dropbox.com/s/b9op9a9p8on5bxo/answer_1.csv?raw=1', 
    'https://www.dropbox.com/s/myvllq0jztm0roh/answer_2.csv?raw=1',
    'https://www.dropbox.com/s/353uttxwgroer6w/answer_3.csv?raw=1',
    'https://www.dropbox.com/s/379t71mtsm3zmwh/answer_4.csv?raw=1', 
    'https://www.dropbox.com/s/idevvpvn9bxfjpc/answer_5.csv?raw=1']
    for pos, link in enumerate(links):
        dict_of_df[f'{pos}_answer'] = pd.read_csv(link)

    return dict_of_df



def main():
    option = st.sidebar.selectbox("Menu: ",
                                  ['Análise', 'Gui Troxa'])
    st.sidebar.markdown('* guarinel@outlook.com \n'
                        '* [LinkedIn](https://www.linkedin.com/in/luizguarinello/) - '
                        '[GitHub](https://github.com/guarinel')

    df = load_train()

    df = df['0_answer'].drop('Unnamed: 0', axis =1)

    values = df['regiao'].unique()

    st.markdown(""" # HACKATON A3DATA
## Objetivo:
Mapear estátisticamente o comportamente dos trabalhadores brasileiros entre 2010 e 2019.
Fonte de dados: Microsdados Rais - GOV BR
#### Primeira Perguntas: Salário Médio nos últimos 10 anos de homens e mulheres que trabalham com tecnologia na regiao Sudeste
Por se tratar de uma área (técnologia) com ampla  interpretacao a metodologia utilizada foi:

* Cargos com a palavra técnologia no nome 

* Cargos com a palavra computação ou computador 

* Cargos classificados em sistema de informação pelo CBO 2002 

Os ranges finais de CBOs selecionados foram 2032, 2123, 1425 ,317, 201, 212, podendo ser completamente customizável.

Gráfixo inicialmente fixo no Sudeste, todas as regiões estão disponíveis para visualização""")


    selected_values = st.multiselect("Selecione Regiao",values)
    if len(selected_values) == 0:
        selected_values = ['SUDESTE']
    filtered_df = df[df['regiao'].isin(selected_values)]

    df_men = filtered_df[filtered_df['sexo'] == 1]
    df_women = filtered_df[filtered_df['sexo'] == 2]

    trace = go.Bar(x=df_men['ano'] ,y=df_men['_col2'],showlegend = True, name = "Homen")
    trace_ = go.Bar(x=df_women['ano'] ,y=df_women['_col2'],showlegend = True, name = 'Mulher')
    layout = go.Layout(title = "Salario Medio de pessoas que trabalham com tecnologia")
    data = [trace, trace_]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()




