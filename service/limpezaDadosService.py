import re
import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from openpyxl.workbook import Workbook


load_dotenv(find_dotenv())


DATASET_DENGUE_CACHOEIRO = os.environ.get("DENGUE_CACHOEIRO")
PASTA_DOUGLAS = os.environ.get("PASTA_DOUGLAS")

if not DATASET_DENGUE_CACHOEIRO:
    print("DATASET_DENGUE_CACHOEIRO não encontrado no arquivo .env")
else:
    print("Caminho do dataset:", DATASET_DENGUE_CACHOEIRO)
    filepath = DATASET_DENGUE_CACHOEIRO

    
    with open(filepath, 'r', encoding='utf-8') as file:
        linhas = file.readlines()


    
    lista_processada = []
    for linha in linhas:
    

        partes = re.findall(r'([a-zA-Z\sáéíóúãõâêîôûçÁÉÍÓÚÃÕÂÊÎÔÛÇ]+|\d+)', linha)

        lista_sem_tabs = [item.replace('\t', '') for item in partes]
        lista_sem_quebra_linha = [item.replace('\n', '') for item in lista_sem_tabs]

        lista_filtrada = [item.replace('Cachoeiro de Itapemirim', '') for item in filter(None, lista_sem_quebra_linha)]


        if linha:  
            lista_processada.append(lista_filtrada)

    




lista_munipicio =[]
lista_semana_epidemiologica =[]
lista_casos_confirmados =[]

for dados in lista_processada[1:]:
    lista_munipicio.append(dados[0])
    lista_semana_epidemiologica.append(dados[1])
    lista_casos_confirmados.append(dados[2])


dataset ={
    'munipicio': lista_munipicio,
    'semana_epidemiologica': lista_semana_epidemiologica,
    'casos_confirmados': lista_casos_confirmados
}

print(len(dataset['munipicio']))


if not PASTA_DOUGLAS:
    print("DATASET_DENGUE_CACHOEIRO não encontrado no arquivo .env")
else:
    print("Caminho do dataset:", PASTA_DOUGLAS)
    output_dir = PASTA_DOUGLAS

df = pd.DataFrame(dataset)


os.makedirs(output_dir, exist_ok=True)  

output_filepath = os.path.join(output_dir, 'dados_processados.xlsx')

df.to_excel(output_filepath, index=False)
print(f"Dados foram salvos no arquivo '{output_filepath}'")