from src.util.arquive_util import read_txt
from src.util.path_util import create_path
from src.util.excel_util import save_to_excel
from src.data.dengue_processed_data import processar_dengue_txt
from dotenv import load_dotenv, find_dotenv
import os


def main():
    load_dotenv(find_dotenv())

    DATASET_DENGUE_2022 = os.environ.get("DENGUE_2022")
    DATASET_DENGUE_2023 = os.environ.get("DENGUE_2023")
    DATASET_DENGUE_2024 = os.environ.get("DENGUE_2024")
    PASTA_DOUGLAS = os.environ.get("PASTA_DOUGLAS")

    lista_path_dataset = []

    if not DATASET_DENGUE_2022 and DATASET_DENGUE_2023 and DATASET_DENGUE_2024:
        print("DATASET_DENGUE_CACHOEIRO não encontrado no arquivo .env")
    else:
        print("Caminho do dataset:", DATASET_DENGUE_2024)
        lista_path_dataset = [DATASET_DENGUE_2022, DATASET_DENGUE_2023, DATASET_DENGUE_2024]
        
    for path in lista_path_dataset:
       linhas = read_txt(path)
       dict_dataset = processar_dengue_txt(linhas)
       path_processed = create_path("processed", PASTA_DOUGLAS)
       save_to_excel(dict_dataset, path_processed, path)
       
       
       
        
if __name__ == "__main__":
    main()


    