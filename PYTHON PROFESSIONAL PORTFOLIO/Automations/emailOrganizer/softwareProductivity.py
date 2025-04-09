def softwares_produtivos(email_usuario, senha, pasta_imap):
    """Lista softwares produtivos encontrados nos emails."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    softwares_interessantes = []

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

                # Ajuste as palavras-chave para o seu perfil e softwares
                palavras_chave_softwares = [
                    "python", "pandas", "selenium", "vscode", "docker",
                    "git", "linux", "cloud", "aws", "azure"
                ]

                if re.search(r"(software|ferramenta|aplicativo)", assunto + corpo):
                    for palavra in palavras_chave_softwares:
                        if palavra in assunto or palavra in corpo:
                            softwares_interessantes.append(assunto)
                            break # Evita duplicatas para um mesmo email.

    print("Softwares Produtivos Encontrados:")
    print(Counter(softwares_interessantes).most_common(10))

    mail.close()
    mail.logout()

softwares_produtivos("seuemail@gmail.com", "suasenha", "INBOX")