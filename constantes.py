escolaridade = {1: 'ANALFABETO',
 2: 'ATÉ 5.A INC',
 3: '5.A CO FUND',
 4: '6. A 9. FUND',
 5: 'FUND COMPL',
 6: 'MÉDIO INCOMP',
 7: 'MÉDIO COMPL',
 8: 'SUP. INCOMP',
 9: 'SUP. COMP',
 10: 'MESTRADO',
 11: 'DOUTORADO',
 -1: 'IGNORADO'}

range_cnaes = [("_".join(["0" + str(x) for x in range(1, 4)]),  "AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AQÜICULTURA"),
("_".join(["0" +  str(x) for x in range(5, 10)]),     "INDÚSTRIAS EXTRATIVAS"),
("_".join([str(x) for x in range(10, 34) ]), " INDÚSTRIAS DE TRANSFORMAÇÃO"),
("_".join([str(x) for x in range(35, 36) ]), " ELETRICIDADE E GÁS"),
("_".join([str(x) for x in range(36, 40) ]), " ÁGUA, ESGOTO, ATIVIDADES DE GESTÃO DE RESÍDUOS E DESCONTAMINAÇÃO"),
("_".join([str(x) for x in range(41, 44) ]), " CONSTRUÇÃO"),
("_".join([str(x) for x in range(45, 48) ]), " COMÉRCIO; REPARAÇÃO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS"),
("_".join([str(x) for x in range(49, 54) ]), " TRANSPORTE, ARMAZENAGEM E CORREIO"),
("_".join([str(x) for x in range(55, 57) ]), " ALOJAMENTO E ALIMENTAÇÃO"),
("_".join([str(x) for x in range(58, 64) ]), " INFORMAÇÃO E COMUNICAÇÃO"),
("_".join([str(x) for x in range(64, 67) ]), " ATIVIDADES FINANCEIRAS, DE SEGUROS E SERVIÇOS RELACIONADOS"),
("_".join([str(x) for x in range(68, 69) ]), " ATIVIDADES IMOBILIÁRIAS"),
("_".join([str(x) for x in range(69, 76) ]), "ATIVIDADES PROFISSIONAIS, CIENTÍFICAS E TÉCNICAS"),
("_".join([str(x) for x in range(77, 83) ]), "ATIVIDADES ADMINISTRATIVAS E SERVIÇOS COMPLEMENTARES"),
("_".join([str(x) for x in range(84, 85) ]), " ADMINISTRAÇÃO PÚBLICA, DEFESA E SEGURIDADE SOCIAL"),
("_".join([str(x) for x in range(85, 86) ]), " EDUCAÇÃO"),
("_".join([str(x) for x in range(86, 89) ]), " SAÚDE HUMANA E SERVIÇOS SOCIAIS"),
("_".join([str(x) for x in range(90, 94) ]), " ARTES, CULTURA, ESPORTE E RECREAÇÃO"),
("_".join([str(x) for x in range(94, 97) ]), " OUTRAS ATIVIDADES DE SERVIÇOS"),
("_".join([str(x) for x in range(97, 98) ]), " SERVIÇOS DOMÉSTICOS"),
("_".join([str(x) for x in range(99, 100)]), "	ORGANISMOS INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS")]