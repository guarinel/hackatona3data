import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns
import streamlit as st
from constantes import *

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

    dict_final = load_train()

    df = dict_final['0_answer'].drop('Unnamed: 0', axis =1)


    st.markdown(""" # HACKATON A3DATA
## Objetivo:
Mapear estatisticamente o comportamento dos trabalhadores brasileiros entre 2010 e 2019.
Fonte de dados: Microdados Rais - GOV BR
#### Primeira Pergunta: Salário Médio nos últimos 10 anos de homens e mulheres que trabalham com tecnologia na região Sudeste
Por se tratar de uma área (tecnologia) com ampla interpretação, a metodologia utilizada foi:

* Cargos com a palavra tecnologia no nome 

* Cargos com a palavra computação ou computador 

* Cargos classificados em sistema de informação pelo CBO 2002 

Os ranges finais de CBOs selecionados foram 2032, 2123, 1425 ,317, 201, 212, podendo variar dependendo da necessidade específica.

Gráfico inicialmente fixo no Sudeste, todas as regiões estão disponíveis para visualização""")

    values = ['SUDESTE', 'CENTRO_OESTE', 'NORDESTE', 'NORTE', 'SUL'] #df['regiao'].unique()

    selected_values = st.selectbox("Selecione a região",values)

    filtered_df = df[df['regiao'] == selected_values]


    df_men = filtered_df[filtered_df['sexo'] == 1]
    df_women = filtered_df[filtered_df['sexo'] == 2]

    trace = go.Bar(x=df_men['ano'] ,y=df_men['_col2'],showlegend = True, name = "Homen")
    trace_ = go.Bar(x=df_women['ano'] ,y=df_women['_col2'],showlegend = True, name = 'Mulher')
    layout = go.Layout(title = "Salário Médio de pessoas que trabalham com tecnologia")
    data = [trace, trace_]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig)

    st.markdown(""" ### Segunda Pergunta: Salário Médio nos últimos 10 anos de pessoas que trabalham no setor de agronegócio
A metodologia utilizada foi:

* CNAE 2002 dentro do range 01, 02, 03. na categoria "COLOCAR CATEGORIA" , podendo variar dependendo da necessidade específica.

Gráfico inicialmente fixo no SUL, todas as regiões estão disponíveis para visualização""")

    df_1 = dict_final['1_answer']
    for key in escolaridade:
        df_1.loc[df_1['escolaridade'] == key, "escolaridade"] = escolaridade[key]
    
    values_ = [ 'SUL' , 'SUDESTE', 'CENTRO_OESTE', 'NORDESTE', 'NORTE']

    selected_values = st.selectbox("Selecione a região",values_)

    filtered_df = df_1[df_1['regiao'] == selected_values]

    df_grouped = filtered_df.groupby("escolaridade").mean()
    df_grouped = df_grouped.sort_values(by = '_col1')

    trace = go.Bar(x=df_grouped.index ,y=df_grouped['_col1'],showlegend = True, name = "Escolaridade")
    layout = go.Layout(title = "Salário Médio de pessoas nos últimos 10 anos por nível de escolaridade")
    data = [trace]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig)

    st.markdown(""" ### Terceira Pergunta: Entre os setores de tecnologia, industria automobilistica e profissionais da saude, qual teve o maior crescimento? Qual quantidade de trabalhadores por ano.
A metodologia utilizada foi:

* CNAE 2002 dentro do range 62 e 63 no setor de tecnologia;
* CNAE 2002 dentro do range 86 e 87 no de indústria automobilística;
* CNAE 2002 dentro do range 45 como profissionais da saúde, todos podendo variar dependendo da necessidade específica.

Gráfico inicialmente fixo no SUL, todas as regiões estão disponíveis para visualização""")

    df_2 = dict_final['2_answer']
    df_2['diff_admi_demi'] = df_2['soma_admissao'] + df_2['soma_demissao'] 

    
    filtered_df_auto = df_2[df_2['setor'] == 'Automobilistica']
    qntd_abs_auto = filtered_df_auto.loc[filtered_df_auto['setor'] == 'Automobilistica'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] - \
    filtered_df_auto.loc[filtered_df_auto['setor'] == 'Automobilistica'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]
    qntd_rel_auto = (filtered_df_auto.loc[filtered_df_auto['setor'] == 'Automobilistica'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] / \
    filtered_df_auto.loc[filtered_df_auto['setor'] == 'Automobilistica'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]) - 1 

    filtered_df_saude = df_2[df_2['setor'] == 'Saude']
    qntd_abs_saude = filtered_df_saude.loc[filtered_df_saude['setor'] == 'Saude'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] - \
    filtered_df_saude.loc[filtered_df_saude['setor'] == 'Saude'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]
    qntd_rel_saude = (filtered_df_saude.loc[filtered_df_saude['setor'] == 'Saude'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] / \
    filtered_df_saude.loc[filtered_df_saude['setor'] == 'Saude'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]) - 1 

    filtered_df_tecn = df_2[df_2['setor'] == 'Tecnologia']
    qntd_abs_tech = filtered_df_tecn.loc[filtered_df_tecn['setor'] == 'Tecnologia'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] - \
    filtered_df_tecn.loc[filtered_df_tecn['setor'] == 'Tecnologia'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]
    qntd_rel_tech = (filtered_df_tecn.loc[filtered_df_tecn['setor'] == 'Tecnologia'].groupby('ano').sum().loc[2019]['qnt_trabalhadores'] / \
    filtered_df_tecn.loc[filtered_df_tecn['setor'] == 'Tecnologia'].groupby('ano').sum().loc[2010][['qnt_trabalhadores']][0]) - 1 


    trace_saude = go.Bar(x=filtered_df_saude['ano'] ,y=filtered_df_saude['qnt_trabalhadores'],showlegend = True, name = "Saude")
    trace_auto = go.Bar(x=filtered_df_auto['ano'] ,y=filtered_df_auto['qnt_trabalhadores'],showlegend = True, name = "Automobilistica")
    trace_tech = go.Bar(x=filtered_df_tecn['ano'] ,y=filtered_df_tecn['qnt_trabalhadores'],showlegend = True, name = "Tecnologia")
    layout = go.Layout(title = "Quantidade de trabalhadores por setor")
    data = [trace_saude, trace_auto, trace_tech]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig)


    values_abs_setores = [qntd_abs_saude, qntd_abs_auto, qntd_abs_tech]
    values_rel_setores = [qntd_rel_saude, qntd_rel_auto, qntd_rel_tech]


    trace_saude_asb = go.Bar(x=['Saúde', 'Automobilístico', 'Tecnologia'] ,y=values_abs_setores,showlegend = True, name = "Crescimento Absoluto")

    layout = go.Layout(title = "Crescimento absoluto em número de trabalhadores entre 2010 e 2019")
    data = [trace_saude_asb]
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig)
    
    trace_auto_rel = go.Bar(x=['Saúde', 'Automobilístico', 'Tecnologia'] ,y=[100*x for x in values_rel_setores],showlegend = True, name = "Automobilistica")
    layout = go.Layout(title = "Crescimento relativo (em %) do número de trabalhadores entre 2010 e 2019")
    data = [trace_auto_rel]
    fig = go.Figure(data=data,layout=layout)
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    st.plotly_chart(fig)

    st.markdown(""" ### Observamos tanto em números absolutos quanto relativos, o setor de saúde demonstrou maior crescimento""")


    st.markdown(""" ### Quarta Pergunta: Nos últimos 10 anos quais foram os setores com o maior número de trabalhadores que possuem jornada semanal inferior a 40h.
A metodologia utilizada foi pegar os grande nove grupos representados pelo primeiro digito do CNAE que são:

* CNAE 2002 dentro do range 62 e 63 no setor de tecnologia;
* CNAE 2002 dentro do range 86 e 87 no de indústria automobilística;
* CNAE 2002 dentro do range 45 como profissionais da saúde, todos podendo variar dependendo da necessidade específica.

TERMINAR""")

    df_3 = dict_final['3_answer']
    for tuple_ in range_cnaes:
        df_3.loc[df_3['cnae_d'].isin([int(x) for x in tuple_[0].split('_')]), 'correspondencia_cnae'] = tuple_[1]

    for ano in df['ano'].unique():
        print(df_3.loc[df_3['ano'] == ano].groupby('correspondencia_cnae').sum().sort_values(by = 'sum_less_than_forty').iloc[-2:])


    st.markdown(""" ### Quinta Pergunta: Nos últimos 10 anos quais foram os setores com o maior número de trabalhadores que possuem jornada semanal inferior a 40h.
A metodologia utilizada foi pegar os grande nove grupos representados pelo primeiro digito do CNAE que são:

* CNAE 2002 dentro do range 62 e 63 no setor de tecnologia;
* CNAE 2002 dentro do range 86 e 87 no de indústria automobilística;
* CNAE 2002 dentro do range 45 como profissionais da saúde, todos podendo variar dependendo da necessidade específica.

TERMINAR""")

    df_3 = dict_final['3_answer']
    for tuple_ in range_cnaes:
        df_3.loc[df_3['cnae_d'].isin([int(x) for x in tuple_[0].split('_')]), 'correspondencia_cnae'] = tuple_[1]

    for ano in df['ano'].unique():
        print(df_3.loc[df_3['ano'] == ano].groupby('correspondencia_cnae').sum().sort_values(by = 'sum_less_than_forty').iloc[-2:])



if __name__ == '__main__':
    main()




