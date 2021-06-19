# hackatona3data

## Fluxo dos arquivos:
 - send_to_s3.py conecta com FTP do governo, extrai arquivos, converte para .parquet e coloca no s3 separado por ano.
 - queryathena.py responsável por orgazinar a ordem e referência das querys e salvar os df com resultados finais.
 - querys_sql.py são 3 views usadas como base para responder as 5 perguntas. Arquitetura das querys em cascata. 30min para calcular todo período.
 - app.py faz visualização e estrutura dash. 
 
## Arquitetura 
 O sistema foi pensado de forma modular. Um serviço focado em extração (send_to_s3.py), toda a parte de parte de transaform foi feita em SQL(query_athena 
+ querys_sql.py ), com o objetivo de usar o melhor de cada linguagem.
- As 3 views criadas pavimentam toda a estrutura do banco de dados para conseguirmos extrair qualquer informação de forma rápida. 

 
## Equipe Mordor
A dashborad pode ser encontrada em https://dash-a3datahackaton.herokuapp.com/.

Luiz Guarinello

Guilherme Dendena
