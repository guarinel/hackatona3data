base_query_1_layout = """
CREATE OR REPLACE VIEW {} AS
SELECT '{}' as ano, 
    "Sexo Trabalhador" as sexo,
    "cbo ocupação 2002" as cbo,
    CAST(TRIM("Escolaridade após 2005") as INT) as escolaridade,
    "CNAE 2.0 Subclasse" as cnae,
    CAST(TRIM("Qtd Hora Contr") as INT) as qntd_hora_contr,
    "Motivo Desligamento" as motivo_desligamento,
    CAST(REPLACE(TRIM("Tempo Emprego"), ',', '.') as DOUBLE) as tempo_emprego_meses,
    CAST(TRIM("Mês Admissão") as INT) as mes_admissao,
    CAST(TRIM("Mês Desligamento") as INT) as mes_desligamento,
    CASE
        WHEN "estado" in ('SP', 'ES', 'MG', 'RJ', 'MG_ES_RJ') THEN 'SUDESTE'
        WHEN "estado" in ('RS', 'SC', 'PR', 'SUL') THEN 'SUL'
        WHEN "estado" in ('MS', 'MT', 'DF', 'GO', 'CENTRO_OESTE') THEN 'CENTRO_OESTE'
        WHEN "estado" in ('RO', 'AC', 'AM', 'RR', 'AP', 'PA', 'TO', 'NORTE') THEN 'NORTE'
        ELSE 'NORDESTE'
    END as regiao,
    CASE
        WHEN CAST(TRIM("Mês Admissão") as INT) > 0 THEN 1
        ELSE 0
    END as soma_admissao,
    CASE
        WHEN CAST(TRIM("Mês Desligamento") as INT) > 0 THEN -1
        ELSE 0
    END as soma_demissao,
    CASE 
        WHEN CAST(TRIM("qtd hora contr") as INT) < 40 THEN 1
        ELSE 0
    END as count_less_than_forty,
    SUBSTRING("CNAE 2.0 Subclasse",1,2)  as cnae_d,
    CAST(REPLACE("vl remun média nom", ',', '.') AS DECIMAL(10,2)) as salario
FROM "a3datahackaton"."{}";"""

second_query_1_layout = """
    CREATE or REPLACE VIEW {} AS
    SELECT "ano", "sexo", "regiao", avg("salario") as media_salario, "cbo", "escolaridade", "cnae"
    FROM "a3datahackaton"."{}"
    WHERE "salario" > 0    
    GROUP BY "ano", "regiao", "sexo", "cbo", "escolaridade", "cnae"; """

third_query_2_layout = """ 
    CREATE or REPLACE VIEW {} AS
    SELECT "cnae_d", "ano", SUM("soma_admissao") as soma_admissao, SUM("soma_demissao") as soma_demissao, SUM("count_less_than_forty") as sum_less_than_forty, COUNT("ano") as qnt_trabalhadores
    FROM "a3datahackaton"."{}"
    GROUP BY "ano" ,"cnae_d"; """


query_q1 = """
    SELECT "sexo", "regiao", avg("media_salario"), "ano"
    FROM "a3datahackaton"."{}" 
    WHERE SUBSTRING("cbo",1, 4) in ('2032', '2123','1425') or SUBSTRING("cbo", 1, 3) in ('317', '201',  '212') 
    GROUP BY "sexo", "regiao", "ano";"""

query_q2 = """
        SELECT "escolaridade",  avg("media_salario"), "regiao", "ano"
        FROM "a3datahackaton"."{}" 
        WHERE SUBSTRING("cnae",1,2) in ('01', '02', '03')
        GROUP BY "escolaridade", "regiao", "ano" ;"""

query_q3 = """
        SELECT "soma_admissao",  "soma_demissao", "cnae_d", "ano", "qnt_trabalhadores",
        CASE 
            WHEN "cnae_d" in ('62', '63') THEN 'Tecnologia'
            WHEN "cnae_d" in ('86','87') THEN 'Saude'
            WHEN "cnae_d" = '45' THEN 'Automobilistica'
            ELSE ''
        END AS setor             
        FROM "a3datahackaton"."{}" 
       WHERE "cnae_d"in ('86', '63', '62', '87','45') ;"""

query_q4 = """
        SELECT SUM("sum_less_than_forty") as sum_less_than_forty, "cnae_d", "ano"
        FROM "a3datahackaton"."{}"
        GROUP BY "cnae_d", "ano"; """

query_q5 = """
    SELECT "Sexo Trabalhador", 
    '{}' as ano,
    SUM(CAST(TRIM("ind trab intermitente") as INT)) as soma_intermitente
    FROM "a3datahackaton"."{}"
    GROUP BY "Sexo Trabalhador"; """
