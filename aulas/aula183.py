# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
import locale
from datetime import datetime
import string
from pathlib import Path

FILE_PATH = Path(__file__).parent
FILE_NAME = 'aula183.txt'
FILE = FILE_PATH / FILE_NAME

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

date = datetime.now()
data = dict(
    nome = 'John Doe',
    valor = converte_para_brl(1_234_456),
    data = date.strftime('%d/%m/%Y'),
    empresa = 'O. M. Company',
    telefone = '+55 (11) 98877-6655'
)

class MyTemplate(string.Template):
    delimiter = '%'

with open(FILE, 'r', encoding='utf-8') as file:
    text = file.read()
    template = string.Template(text)
    print(template.safe_substitute(data))


