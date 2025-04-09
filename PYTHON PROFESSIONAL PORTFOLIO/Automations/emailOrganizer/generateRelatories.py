import imaplib
import email
from collections import Counter

def gerar_relatorio_emails(email_usuario, senha, pasta_imap):
    """Gera um relatório com estatísticas dos emails."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    remetentes = []
    assuntos = []
    for num in data[0].split():
        _, data = mail.fetch(num, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                remetentes.append(msg["from"])
                assuntos.append(msg["subject"])

    print("Relatório de Emails:")
    print(f"Total de emails: {len(remetentes)}")
    print(f"Remetentes mais frequentes: {Counter(remetentes).most_common(5)}")
    print(f"Assuntos mais comuns: {Counter(assuntos).most_common(5)}")
    mail.close()
    mail.logout()

gerar_relatorio_emails("seuemail@gmail.com", "suasenha", "INBOX")