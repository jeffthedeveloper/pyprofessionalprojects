import imaplib
import email
import os

def processar_emails(email_usuario, senha, pasta_imap, pasta_destino):
    """Processa e organiza e-mails usando IMAP."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com") # ou outro servidor imap
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    for num in data[0].split():
        _, data = mail.fetch(num, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                assunto = msg["subject"]
                # Crie regras para classificar emails aqui
                if "trabalho" in assunto.lower():
                    destino = os.path.join(pasta_destino, "trabalho")
                elif "casa" in assunto.lower():
                    destino = os.path.join(pasta_destino, "casa")
                # ... mais regras
                else:
                    destino = os.path.join(pasta_destino, "geral")

                os.makedirs(destino, exist_ok=True) # Cria os diretorios caso nao existam
                # Salvar o email em um arquivo
                with open(os.path.join(destino, f"{num.decode()}.eml"), "wb") as f:
                    f.write(response_part[1])
    mail.close()
    mail.logout()

# Substitua com suas informações
processar_emails("seuemail@gmail.com", "suasenha", "INBOX", "emails_organizados")