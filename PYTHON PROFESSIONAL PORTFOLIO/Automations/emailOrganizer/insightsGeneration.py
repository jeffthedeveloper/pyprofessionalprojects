import imaplib
import email
from collections import Counter
import re

def gerar_insights_emails(email_usuario, senha, pasta_imap):
    """Gera insights detalhados dos emails."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    campanhas = []
    vagas = []
    cursos = []
    eventos = []
    softwares = []
    palestras = []
    consultorias = []
    propagandas = []
    outros = []

    for num in data[0].split():
        _, data = mail.fetch(num, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                corpo = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            corpo = part.get_payload(decode=True).decode()
                else:
                    corpo = msg.get_payload(decode=True).decode()
                assunto = msg["subject"].lower()
                corpo = corpo.lower()

                if re.search(r"(campanha|promoção|desconto)", assunto + corpo):
                    campanhas.append(assunto)
                elif re.search(r"(vaga|emprego|oportunidade)", assunto + corpo):
                    vagas.append(assunto)
                elif re.search(r"(curso|treinamento|educação)", assunto + corpo):
                    cursos.append(assunto)
                elif re.search(r"(evento|workshop|conferência)", assunto + corpo):
                    eventos.append(assunto)
                elif re.search(r"(software|ferramenta|aplicativo)", assunto + corpo):
                    softwares.append(assunto)
                elif re.search(r"(palestra|seminário|webinar)", assunto + corpo):
                    palestras.append(assunto)
                elif re.search(r"(consultoria|assessoria|mentor)", assunto + corpo):
                    consultorias.append(assunto)
                elif re.search(r"(propaganda|anúncio|publicidade)", assunto + corpo):
                    propagandas.append(assunto)
                else:
                    outros.append(assunto)

    print("Insights dos Emails:")
    print(f"Campanhas/Promoções: {Counter(campanhas).most_common(5)}")
    print(f"Vagas de Emprego: {Counter(vagas).most_common(5)}")
    print(f"Cursos/Treinamentos: {Counter(cursos).most_common(5)}")
    print(f"Eventos/Workshops: {Counter(eventos).most_common(5)}")
    print(f"Softwares/Ferramentas: {Counter(softwares).most_common(5)}")
    print(f"Palestras/Seminários: {Counter(palestras).most_common(5)}")
    print(f"Consultorias/Mentorias: {Counter(consultorias).most_common(5)}")
    print(f"Propagandas: {Counter(propagandas).most_common(5)}")
    print(f"Outros: {Counter(outros).most_common(5)}")

    mail.close()
    mail.logout()

gerar_insights_emails("seuemail@gmail.com", "suasenha", "INBOX")