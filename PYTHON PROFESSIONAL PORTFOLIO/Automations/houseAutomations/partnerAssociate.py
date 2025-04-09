from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import smtplib
from email.mime.text import MIMEText

def gerar_cartao(nome, numero_socio, arquivo_pdf):
    c = canvas.Canvas(arquivo_pdf, pagesize=letter)
    c.drawString(100, 750, f"Cartão de Sócio")
    c.drawString(100, 730, f"Nome: {nome}")
    c.drawString(100, 710, f"Número: {numero_socio}")
    c.save()

def enviar_email(destinatario, arquivo_pdf):
    msg = MIMEText("Seu cartão de sócio em anexo.")
    msg["Subject"] = "Cartão de Sócio"
    msg["From"] = "SEU_EMAIL"
    msg["To"] = destinatario

    with smtplib.SMTP("smtp.gmail.com", 587) as server: # Ou outro servidor SMTP
        server.starttls()
        server.login("SEU_EMAIL", "SUA_SENHA")
        server.sendmail("SEU_EMAIL", destinatario, msg.as_string())

gerar_cartao("João Silva", "12345", "cartao_joao.pdf")
enviar_email("joao@email.com", "cartao_joao.pdf")