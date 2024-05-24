from src.data import dengue_processed_data
from src.util import request_util
from dotenv import load_dotenv, find_dotenv
from src.data import cidadao_precessed_data
from src.util.excel_util import save_to_excel
from src.util import path_util
import os

v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []
v8 = []
v9 = []
v10 = []
v11 = []
v12 = []
v13 = []
v14 = []
v15 = []
v16 = []
v17 = []



def execute(data):
    load_dotenv(find_dotenv())
    URL_GEOSAPI = os.environ.get("URL_GEOSAPI")
    PASTA_DOUGLAS = os.environ.get("PASTA_DOUGLAS")
    for d in data:
        html = request_util.method_post(URL_GEOSAPI,d)
        table_data = cidadao_precessed_data.processar_cidadao_html(html)

        v1.append(table_data["Total de famílias cadastradas"])
        v2.append(table_data["Total de famílias com até 2 anos de atualização no cadastro"])
        v3.append(table_data["Total de famílias em situação de Extrema Pobreza"])
        v4.append(table_data["Total de famílias em situação de Pobreza"])
        v5.append(table_data["Total de famílias de Baixa Renda"])
        v6.append(table_data["Total de famílias com renda per capita acima de ½ S.M."])
        v7.append(table_data["Total de famílias com benefícios do PBF"])
        v8.append(table_data["Total de famílias com informação de membros com deficiência"])
        v9.append(table_data["Total de pessoas cadastradas"])
        v10.append(table_data["Total de pessoas pertencentes a famílias beneficiárias PBF"])
        v11.append(table_data["Total de pessoas com idade entre 0 e 3 anos"])
        v12.append(table_data["Total de pessoas com idade entre 4 e 6 anos"])
        v13.append(table_data["Total de pessoas com idade entre 7 e 10 anos"])
        v14.append(table_data["Total de pessoas com idade entre 11 e 15 anos"])
        v15.append(table_data["Total de pessoas com idade entre 16 e 19 anos"])
        v16.append(table_data["Total de pessoas com idade entre 20 e 24 anos"])
        v17.append(table_data["Total de pessoas com idade de 60 anos ou mais"])
    

    dataset = {
        'Total de famílias cadastradas': v1,
        'Total de famílias com até 2 anos de atualização no cadastro': v2,
        'Total de famílias em situação de Extrema Pobreza': v3,
        'Total de famílias em situação de Pobreza': v4,
        'Total de famílias de Baixa Renda': v5,
        'Total de famílias com renda per capita acima de ½ S.M.': v6,
        'Total de famílias com benefícios do PBF': v7,
        'Total de famílias com informação de membros com deficiência': v8,
        'Total de pessoas cadastradas': v9,
        'Total de pessoas pertencentes a famílias beneficiárias PBF': v10,
        'Total de pessoas com idade entre 0 e 3 anos': v11,
        'Total de pessoas com idade entre 4 e 6 anos': v12,
        'Total de pessoas com idade entre 7 e 10 anos': v13,
        'Total de pessoas com idade entre 11 e 15 anos': v14,
        'Total de pessoas com idade entre 16 e 19 anos': v15,
        'Total de pessoas com idade entre 20 e 24 anos': v16,
        'Total de pessoas com idade de 60 anos ou mais': v17
    }
   

    path_processed = path_util.create_path("processed", PASTA_DOUGLAS)
    save_to_excel(dataset, path_processed, PASTA_DOUGLAS + "/cidadao_cadunico_2019.xlsx")
    
    
data = ["320120930000003","320120905000227"]

execute(data)

