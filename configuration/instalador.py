import os
import requests
import shutil
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

def load_environment_variables():
    load_dotenv(find_dotenv())
    return os.environ.get("FIREFOX"), os.environ.get("MARIONETE")

def create_tools_folder(project_folder):
    tools_folder = project_folder / "ferramentas"
    if not tools_folder.exists():
        tools_folder.mkdir()
        print(f"Pasta 'ferramentas' criada com sucesso em '{project_folder}'.")
    else:
        print(f"A pasta 'ferramentas' já existe em '{project_folder}'.")
    return tools_folder

def download_and_save_file(url, destination_folder, filename):
    file_path = destination_folder / filename
    with requests.get(url, stream=True) as response:
        with open(file_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    return file_path

def execute():
    # Carrega as variáveis de ambiente
    FIREFOX, MARIONETE = load_environment_variables()

    # Define a pasta do projeto
    project_folder = Path(__file__).parent

    # Cria a pasta 'ferramentas' no projeto
    tools_folder = create_tools_folder(project_folder)

    # Baixa e salva o geckodriver na pasta 'ferramentas'
    geckodriver_filename = "geckodriver.tar.gz"
    geckodriver_path = download_and_save_file(FIREFOX, tools_folder, geckodriver_filename)

    # Baixa e salva o Firefox na pasta 'ferramentas'
    firefox_filename = "firefox.tar.gz"
    firefox_path = download_and_save_file(MARIONETE, tools_folder, firefox_filename)

    print("Downloads completos e arquivos adicionados à pasta 'ferramentas' do projeto.")
    print("INSTALE O FIREFOX")
    print("CRIE UMA VARIAVEL DE SISTEMA PARA O GECKODRIVER")
    print("EXECUTE O SCRIPT 'BOT_DOWNLOAD_DADOS.PY'")

