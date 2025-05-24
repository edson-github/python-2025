# ZIP - Compactando/Descompactando arquivos com zipfile.ZipFile

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# CAMINHO_ZIP = Path(__file__).parent / 'aula186_arquivos.zip'
# CAMINHO_PASTA = Path(__file__).parent / 'aula186_arquivos'

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula186_zip_dir'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_DESCOMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception('STOP')

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

# Cria os arquivos para a aula
def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s.txt' % i
        with open(zip_dir / f'{texto}', 'w') as arquivo:
            arquivo.write(texto)

criar_arquivos(10, CAMINHO_ZIP_DIR)
# Compactando arquivos com ZipFile
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            caminho_completo = os.path.join(root, file)
            zip.write(
                caminho_completo,
                arcname=os.path.relpath(caminho_completo, CAMINHO_ZIP_DIR)
            )
# Descompactando arquivos com ZipFile
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
        caminho_salvar = CAMINHO_DESCOMPACTADO / arquivo
        # Create parent directories if they don't exist
        caminho_salvar.parent.mkdir(parents=True, exist_ok=True)
        with open(caminho_salvar, 'wb') as new_file:
            with zip.open(arquivo) as old_file:
                shutil.copyfileobj(old_file, new_file)

