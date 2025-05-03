# Enviando e-mails com Python utlizando a SMTP

import os 
import pathlib
from string import Template
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

# Dados remetente e destinatário
REMETENTE = os.getenv('FROM_EMAIL', '')
DESTINATARIO = REMETENTE

# Configuração do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = REMETENTE
SMTP_PASSWORD = os.getenv('EMAIL_PASSWORD', '')

# Caminho arquivo HTML
HTML_FILE = 'classes/aula185.html'

# Mensagem texto 
with open(HTML_FILE, 'r') as file:
    HTML_CONTENT = file.read()
    template = Template(HTML_CONTENT)
    corpo_msg = template.substitute(nome='Edson Andrade')

# Criando a mensagem
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Teste de envio de e-mail'
msg['From'] = REMETENTE
msg['To'] = DESTINATARIO

# Adicionando o corpo HTML
parte_html = MIMEText(corpo_msg, 'html')
msg.attach(parte_html)

# Enviando o email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
    print('Email enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar email: {e}')