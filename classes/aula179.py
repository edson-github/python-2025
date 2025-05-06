# csv.reader() e csv.DictReader()
# csv.reader lê o csv em formato de lista, com cada valor sendo um item dessa lista.
# csv.DictReader lê o arquivo no formato de dicionário.
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'data.csv'

with open(PATH_CSV, 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        print(linha['Nome'], linha['Idade'], linha['Profissão'])

    



    
   