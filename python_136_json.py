from python_136_json_dados import *
import json

# dados_json = json.dumps(clientes_dicionario)
# print(dados_json)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)


