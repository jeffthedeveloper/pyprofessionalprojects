import requests
import time

def obter_taxa_cambio(moeda_base, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_base}"
    response = requests.get(url).json()
    return response["rates"][moeda_destino]

taxa_desejada = 1.10
while True:
    taxa_atual = obter_taxa_cambio("USD", "EUR")
    if taxa_atual <= taxa_desejada:
        print(f"Taxa atingiu {taxa_atual}")
        # Enviar notificação (usando notificaçoes do SO ou email).
        break
    time.sleep(60) # Verifica a cada minuto.