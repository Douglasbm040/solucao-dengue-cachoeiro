import os
import sys

# Obtendo o diretório pai do diretório atual (onde está o arquivo imports_src.py)
diretorio_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Adicionando o diretório atual ao início de sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Adicionando o diretório 'src' ao sys.path
sys.path.append(os.path.join(diretorio_projeto, 'src'))

import src
