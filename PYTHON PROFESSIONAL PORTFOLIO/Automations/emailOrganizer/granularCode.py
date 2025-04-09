import imaplib
import email
import os
import re
import pandas as pd
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

def processar_emails_financeiros(email_usuario, senha, pasta_imap, pasta_destino, arquivo_excel):
    """Processa e categoriza emails financeiros, extrai valores, e gera relatórios."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_usuario, senha)
    mail.select(pasta_imap)
    _, data = mail.search(None, "ALL")

    dados = defaultdict(list)
    categorias = {
        "Ofertas Financeiras": r"(oferta|crédito|financiamento)",
        "Cobranças": r"(fatura|boleto|conta|pagamento)",
        "Investimentos": r"(investimento|ações|renda fixa)",
        "Entretenimento": r"(cinema|show|teatro|evento)",
        "Furadas": r"(fraude|golpe|esquema)",
        "Outros": r"." # Captura tudo que não se encaixar acima
    }
    moedas = {
        "USD": r"\$", "BRL": r"R\$", "EUR": r"€", "GBP": r"£", "CNY": r"¥", "RUB": r"₽"
    }

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

                texto_completo = assunto + corpo
                valor_total = 0.0
                moedas_encontradas = set()

                for moeda, padrao_moeda in moedas.items():
                    padrao = rf"{padrao_moeda}\s*(\d+(?:,\d{{3}})*(?:\.\d{{2}})?)"
                    valores = re.findall(padrao, texto_completo)
                    for val in valores:
                        valor = float(val.replace(".", "").replace(",", "."))
                        valor_total += valor
                        moedas_encontradas.add(moeda)

                if valor_total > 0: # somente se encontrar valores monetários.
                    dados["Assunto"].append(assunto)
                    dados["Valor"].append(valor_total)
                    dados["Moedas"].append(", ".join(moedas_encontradas))
                    for categoria, padrao_categoria in categorias.items():
                        if re.search(padrao_categoria, texto_completo):
                            destino = os.path.join(pasta_destino, categoria)
                            os.makedirs(destino, exist_ok=True)
                            with open(os.path.join(destino, f"{num.decode()}.eml"), "wb") as f:
                                f.write(response_part[1])
                            dados["Categoria"].append(categoria)
                            break # Encontrou uma categoria, sai do loop
                    else: # Se não encontrar nenhuma, classifica como outros.
                        dados["Categoria"].append('Outros')

    mail.close()
    mail.logout()

    df = pd.DataFrame(dados)
    df.to_excel(arquivo_excel, index=False)
    analisar_dados(df)

def analisar_dados(df):
    """Analisa dados e gera relatórios."""
    categorias_gastos = df["Categoria"].value_counts(normalize=True) * 100
    print("Tendências Financeiras:")
    print(categorias_gastos)

    plt.figure(figsize=(10, 6))
    categorias_gastos.plot(kind="bar")
    plt.title("Distribuição de Gastos por Categoria")
    plt.ylabel("Percentual")
    plt.savefig("distribuicao_gastos.png")

    print("\nValores Totais por Moeda:")
    print(df.groupby("Moedas")["Valor"].sum())

    plt.figure(figsize=(10, 6))
    df.groupby('Categoria')['Valor'].sum().sort_values().plot(kind='barh')
    plt.title('Valor Total por Categoria')
    plt.xlabel('Valor Total')
    plt.ylabel('Categoria')
    plt.savefig("valor_por_categoria.png")

# Configurações
email_usuario = "seuemail@gmail.com"
senha = "suasenha"
pasta_imap = "INBOX"
pasta_destino = "emails_financeiros"
arquivo_excel = "emails_financeiros.xlsx"

processar_emails_financeiros(email_usuario, senha, pasta_imap, pasta_destino, arquivo_excel)