# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

# class EscritorCsv:
#     def __init__(self, arquivo):
#         self.arquivo = arquivo
#     def __enter__(self):
#         self.arquivo_csv = open(self.arquivo, 'w')
#         self.writer = csv.writer(self.arquivo_csv, lineterminator='\n')
#         return self.writer
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.arquivo_csv.close()
#         return True
# with EscritorCsv('aula180.csv') as escritor_csv:
#     escritor_csv.writerow(['nome', 'idade', 'nota'])
#     escritor_csv.writerow(['Ana', '25', '9.5'])

# lista_clientes = [
#     {'nome': 'Ana', 'idade': 25, 'nota': 9.5},
#     {'nome': 'João', 'idade': 30, 'nota': 8.7},
#     {'nome': 'Maria', 'idade': 20, 'nota': 9.0},
# ]

# with open(CAMINHO_CSV, 'w') as arquivo_csv:
#     nome_colunas = lista_clientes[0].keys()
#     escritor_csv = csv.DictWriter(
#         arquivo_csv,
#         fieldnames=nome_colunas,
#         lineterminator='\n'
#     )

#     escritor_csv.writeheader()
#     for cliente in lista_clientes:
#         escritor_csv.writerow(cliente)

lista_clientes = [ 
    {'Nome': 'João', 'Endereço': 'Rua 1', 'Telefone': '1111-1111'},
    {'Nome': 'Maria', 'Endereço': 'Rua 2', 'Telefone': '2222-2222'},
    {'Nome': 'José', 'Endereço': 'Rua 3', 'Telefone': '3333-3333'},
    {'Nome': 'Ana', 'Endereço': 'Rua 4', 'Telefone': '4444-4444'},
    {'Nome': 'Pedro', 'Endereço': 'Rua 5', 'Telefone': '5555-5555'},

]

with open(CAMINHO_CSV, 'w') as arquivo_csv:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo_csv,
        fieldnames=nome_colunas,
        lineterminator='\n'
    )
    escritor.writeheader()
    for cliente in lista_clientes:
        escritor.writerow(cliente)


    for cliente in lista_clientes:
        print(cliente)

