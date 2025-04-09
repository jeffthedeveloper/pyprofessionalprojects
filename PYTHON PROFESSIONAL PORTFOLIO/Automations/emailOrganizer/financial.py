import imaplib
import email
import os
import re

def categorizar_emails_financeiros(email_usuario, senha, pasta_imap, pasta_destino):
    """Categoriza emails com cifrões para análise financeira."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    for num in data[0].split():
        _, data = mail.fetch(num, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                assunto = msg["subject"].lower()
                corpo = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            corpo = part.get_payload(decode=True).decode().lower()
                else:
                    corpo = msg.get_payload(decode=True).decode().lower()

                if re.search(r"(\$|r\$)", assunto + corpo):
                    destino = os.path.join(pasta_destino, "financeiro")
                    os.makedirs(destino, exist_ok=True)
                    with open(os.path.join(destino, f"{num.decode()}.eml"), "wb") as f:
                        f.write(response_part[1])

    mail.close()
    mail.logout()

# Substitua com suas informações
categorizar_emails_financeiros("seuemail@gmail.com", "suasenha", "INBOX", "emails_organizados")