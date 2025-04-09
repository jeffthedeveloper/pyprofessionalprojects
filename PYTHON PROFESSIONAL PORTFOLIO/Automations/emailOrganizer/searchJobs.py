import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def buscar_vagas(email_usuario, senha, palavras_chave, localizacao, email_alerta):
    """Busca vagas e envia alertas por email."""
    url = f"URL_DO_SITE_DE_VAGAS?q={palavras_chave}&l={localizacao}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    vagas = soup.find_all("div", class_="vaga")

    for vaga in vagas:
        titulo = vaga.find("h2").text.strip()
        descricao = vaga.find("p").text.strip()
        if "python" in descricao.lower() and "senior" in descricao.lower():
            mensagem = f"Vaga encontrada: {titulo}\n{descricao}"
            enviar_email(email_usuario, senha, email_alerta, "Vaga Encontrada", mensagem)

def enviar_email(email_usuario, senha, destinatario, assunto, mensagem):
    msg = MIMEText(mensagem)
    msg["Subject"] = assunto
    msg["From"] = email_usuario
    msg["To"] = destinatario
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # ou outro servidor
        server.login(email_usuario, senha)
        server.sendmail(email_usuario, destinatario, msg.as_string())

buscar_vagas("seuemail@gmail.com", "suasenha", "desenvolvedor python senior", "sao paulo", "emaildealerta@gmail.com")