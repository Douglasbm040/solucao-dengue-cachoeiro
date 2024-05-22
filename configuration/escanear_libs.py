import os
import re

def encontrar_bibliotecas(diretorio):
    
    bibliotecas = set()
    padrao_import = re.compile(r'^\s*(import|from)\s+(\w+)')

    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.py'):
                caminho_arquivo = os.path.join(root, file)
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    for linha in f:
                        match = padrao_import.match(linha)
                        if match:
                            bibliotecas.add(match.group(2))
    
    return bibliotecas

def encontrar_modulos_local(diretorio):
    modulos_local = set()
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.py'):
                modulo = os.path.splitext(file)[0]
                modulos_local.add(modulo)
    return modulos_local




def libs_do_projeto():
    print("Bibliotecas externas encontradas:")
    # Diretório alvo um nível acima do diretório do script
    diretorio_alvo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Encontra bibliotecas e módulos locais
    bibliotecas_encontradas = encontrar_bibliotecas(diretorio_alvo)
    modulos_locais = encontrar_modulos_local(diretorio_alvo)

    # Filtra somente as bibliotecas externas
    bibliotecas_externas = bibliotecas_encontradas - modulos_locais
    list_libs = []
    for biblioteca in sorted(bibliotecas_externas):
        list_libs.append(biblioteca)
    return list_libs
