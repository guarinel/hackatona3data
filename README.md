# hackaton a3data

## Equipe Mordor

## Fluxo dos arquivos:
 - send_to_s3.py conecta com FTP do governo, extrai arquivos, converte para .parquet e coloca no s3 separado por ano.
 - query_athena.py é responsável por orgazinar a ordem e as referências em cascata das querys no athena, conectar com os servicos AWS, concatenar todos os anos e salvar os dataframes com os resultados finais.
 - querys_sql.py são 3 grande views usadas como base para responder as 5 perguntas cada com uma query simples. Arquitetura das querys em cascata.
 - app.py faz visualização e estrutura dash. 
 
## Arquitetura 
 O sistema foi pensado de forma modular. Um serviço focado em extração (send_to_s3.py), quase toda parte de transform foi feita em SQL(query_athena + querys_sql.py ), com o objetivo de usar o melhor de cada linguagem. 
Python foi usada para conexões entre serviços, automação de processos, análise exploratória e visualização dos dados.
- As 3 views criadas inicalmente no querys_sql.py pavimentam toda a estrutura do banco de dados para conseguirmos extrair qualquer informação de forma rápida. 

Foi feita uma análise exploratória dos dados em python, com objetivo de entender a documentação e projetar os serviços necessários. Todo estudo foi relizados apenas em cima do Acre (ou região Norte) em cada um dos diferentes layouts, permitindo que generalizassemos os processos sem necessidade de custo extra com computação.

A dashborad pode ser encontrada em https://dash-a3datahackaton.herokuapp.com/.

Pitch: https://www.youtube.com/watch?v=LNH9sCa6C1o

Demo: https://www.youtube.com/watch?v=Ue6PisebO8g

Luiz Guarinello

Guilherme Dendena
