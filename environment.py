"""
Arquivo que faz o carregamento das variáveis de ambiente
Faz a leitura do arquivo .env na raiz do projeto
Para utilizar faça o import do mesmo nos seguintes formatos:

1) para importar todas as variaveis de ambiente
from environment import *

"""

from dotenv import dotenv_values

config = dotenv_values('.env')
