import re
import os
import sys



# Função para processar o arquivo
def processar_dengue_txt(linhas):
    lista_processada = []
    for linha in linhas:
        partes = re.findall(r'([a-zA-Z\sáéíóúãõâêîôûçÁÉÍÓÚÃÕÂÊÎÔÛÇ.]+|\d+)', linha)
        lista_sem_tabs = [item.replace('\t', '') for item in partes]
        lista_sem_quebra_linha = [item.replace('\n', '') for item in lista_sem_tabs]
        lista_filtrada = [item.replace('Cachoeiro de Itapemirim', '') for item in filter(None, lista_sem_quebra_linha)]
        print(lista_filtrada)
        if linha:  
            lista_processada.append(lista_filtrada)

    lista_municipio = []
    lista_semana_epidemiologica = []
    lista_casos_confirmados = []

    for dados in lista_processada[1:]:
        lista_municipio.append(dados[0])
        lista_semana_epidemiologica.append(dados[1])
        lista_casos_confirmados.append(dados[2])

    dataset = {
        'municipio': lista_municipio,
        'semana_epidemiologica': lista_semana_epidemiologica,
        'casos_confirmados': lista_casos_confirmados
    }

    return dataset


