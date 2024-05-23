import os


def create_path(nome_pasta, caminho_pai):
    caminho_pasta = os.path.join(caminho_pai, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso em '{caminho_pai}'.")
    else:
        print(f"A pasta '{nome_pasta}' já existe em '{caminho_pai}'.")
    return caminho_pasta

