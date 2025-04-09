import imaplib
import email
import os

def organizar_emails(email_usuario, senha, pasta_imap, pasta_destino):
    """Organiza emails em pastas com base em regras."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com") # ou outro servidor IMAP
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    for num in data[0].split():
        _, data = mail.fetch(num, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                assunto = msg["subject"].lower()
                remetente = msg["from"].lower()
                destino = pasta_destino

                if "trabalho" in assunto or "trabalho" in remetente:
                    destino = os.path.join(destino, "trabalho")
                elif "casa" in assunto or "casa" in remetente:
                    destino = os.path.join(destino, "casa")
                elif "vaga" in assunto or "emprego" in assunto:
                    destino = os.path.join(destino, "emprego")
                # ... mais regras

                os.makedirs(destino, exist_ok=True)
                with open(os.path.join(destino, f"{num.decode()}.eml"), "wb") as f:
                    f.write(response_part[1])
    mail.close()
    mail.logout()

# Substitua com suas informações
organizar_emails("seuemail@gmail.com", "suasenha", "INBOX", "emails_organizados")