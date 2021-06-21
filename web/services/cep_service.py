#Arquivo responsável em armazenar o código que vai consumir a API do viacep e retornar a requisição
#E depois tratar os erros

import requests

def buscar_cidade_cep(cep):
    response = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )
    return response