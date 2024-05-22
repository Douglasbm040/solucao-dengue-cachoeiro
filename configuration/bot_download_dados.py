import os
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv, find_dotenv
import patoolib

def criar_pasta(nome_pasta, caminho_pai):
    caminho_pasta = os.path.join(caminho_pai, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso em '{caminho_pai}'.")
    else:
        print(f"A pasta '{nome_pasta}' já existe em '{caminho_pai}'.")
    return caminho_pasta

def configurar_driver(download_folder):
    options = Options()
    options.set_preference("browser.download.folderList", 2)  # 0: Padrão, 1: Desktop, 2: Pasta personalizada
    options.set_preference("browser.download.dir", download_folder)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip,application/octet-stream")
    return webdriver.Firefox(options=options)

def baixar_e_extrair_arquivos(url, texto_especifico, download_folder, caminho_pasta_dados):
    driver = configurar_driver(download_folder)
    try:
        driver.get(url)
        sleep(15)  # Ajuste o tempo de espera conforme necessário
        div_xpath = f"//div[contains(text(), '{texto_especifico}')]"
        driver.find_element(By.XPATH, div_xpath).click()
        
        # Esperar o download completar
        sleep(30)  # Ajuste o tempo de espera conforme necessário
        
        arquivos = os.listdir(download_folder)
        arquivos_zip = [arquivo for arquivo in arquivos if arquivo.endswith('.zip')]
        
        if not arquivos_zip:
            print("Nenhum arquivo .zip foi encontrado na pasta de downloads.")
            return

        arquivo_zip = os.path.join(download_folder, arquivos_zip[0])
        patoolib.extract_archive(arquivo_zip, outdir=caminho_pasta_dados)
        print("Extração do arquivo .zip concluída.")
    finally:
        #driver.quit()
        print("O navegador foi encerrado.")

def execute():
    load_dotenv(find_dotenv())
    SECRET_KEY = os.environ.get("LINK_DRIVE")
    if not SECRET_KEY:
        print("Link do drive não encontrado no arquivo .env")
        return

    script_directory = os.path.dirname(os.path.abspath(__file__))
    nome_pasta_dados = "repositories"
    caminho_pasta_dados = criar_pasta(nome_pasta_dados, script_directory)
    download_folder = caminho_pasta_dados
    texto_especifico = "Fazer download de tudo"
    url = SECRET_KEY
    baixar_e_extrair_arquivos(url, texto_especifico, download_folder, caminho_pasta_dados)

execute()
