#Imports
import requests
import zipfile
import shutil
import os
import pandas as pd

class dadosCenso():
    
    extract_to = 'descompactado'

    def obterDados(self):
        url = 'https://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_do_Universo/Agregados_por_Setores_Censitarios/ES_20231030.zip'  
        response = requests.get(url)
        zip_file_path = 'arquivo.zip'

        with open(zip_file_path, 'wb') as f:
            f.write(response.content)

        os.makedirs(self.extract_to, exist_ok=True)
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.extract_to)

        print(f'Arquivo extraído para {self.extract_to}')

    def apagarArquivosDesnecessarios(self):
        caminho_da_pasta = self.extract_to + "/Base informaçoes setores2010 universo ES/CSV"

        if os.path.exists(caminho_da_pasta):
            shutil.rmtree(caminho_da_pasta)
            print(f'A pasta "{caminho_da_pasta}" foi apagada com sucesso.')
        else:
            print(f'A pasta "{caminho_da_pasta}" não existe.')

        if os.path.exists('arquivo.zip'):
            os.remove('arquivo.zip')
            print(f'O arquivo arquivo.zip foi apagado com sucesso.')
        else:
            print(f'O arquivo arquivo.zip não existe.')


    def limparDados(self):
        colunas_especificas = ['Cod_setor', 'V002', 'V005', 'V006', 'V007', 'V008', 'V009', 'V010', 'V011', 'V012', 'V013']

        df_principal = pd.read_excel(self.extract_to + '/Base informaçoes setores2010 universo ES\EXCEL\DomicilioRenda_ES.XLS', usecols=colunas_especificas).apply(pd.to_numeric, errors='coerce')

        #filtar apenas linhas que correspondem a Cachoeiro de itapemirim
        df_auxiliar = pd.read_excel(self.extract_to + '/Base informaçoes setores2010 universo ES\EXCEL\Basico_ES.XLS', usecols=['Cod_setor', 'Cod_municipio', 'Nome_do_municipio'])
        df_auxiliar = df_auxiliar[df_auxiliar['Cod_municipio'] == 3201209] #Cahoeiro de itapemirim

        df_principal = df_principal[df_principal['Cod_setor'].isin(df_auxiliar['Cod_setor'])]

        df_principal['Total_Domicilios'] = df_principal[['V005', 'V006', 'V007', 'V008', 'V009', 'V010', 'V011', 'V012', 'V013']].sum(axis=1, skipna=True)
        df_principal['Renda_Media'] = df_principal['V002'] / df_principal['Total_Domicilios']
        return df_principal
    
    def dataFrameParaExcel(self, df):
        df.to_excel("dados_censo2010.xlsx", index=False)
    
    def executar(self):
        self.obterDados()
        self.apagarArquivosDesnecessarios()
        df = self.limparDados()
        self.dataFrameParaExcel(df=df)

dadosCenso = dadosCenso()
dadosCenso.executar()

