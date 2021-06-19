# hackatona3data

## Fluxo dos arquivos:
 - send_to_s3.py conecta com FTP do governo, extrai arquivos, converte para .parquet e coloca no s3 separado por ano.
 - query_athena.py é responsável por orgazinar a ordem e referência das querys no athena, conetar com os servicos AWS e salvar os dataframes com resultados finais.
 - querys_sql.py são 3 grande views usadas como base para responder as 5 perguntas cada com uma query simples. Arquitetura das querys em cascata. 30min para calcular todo período.
 - app.py faz visualização e estrutura dash. 
 
## Arquitetura 
 O sistema foi pensado de forma modular. Um serviço focado em extração (send_to_s3.py), toda a parte de parte de transform foi feita em SQL(query_athena 
+ querys_sql.py ), com o objetivo de usar o melhor de cada linguagem. 
+ Python foi usada para conexões entre serviços, automação de processos, análise exploratória e visualização dos dados.
- As 3 views criadas inicalmente pavimentam toda a estrutura do banco de dados para conseguirmos extrair qualquer informação de forma rápida. 

Foi feita uma análise exploratória dos dados em python, com objetivo de entender a documentação e projetar os serviços necessários. Todo estudo foi relizados apenas em cima do Acre (ou região Norte) em cada um dos diferentes layouts, permitindo que generalizassemos os processos sem necessidade de custo extra com computação.

## Equipe Mordor
A dashborad pode ser encontrada em https://dash-a3datahackaton.herokuapp.com/.

Luiz Guarinello

Guilherme Dendena
