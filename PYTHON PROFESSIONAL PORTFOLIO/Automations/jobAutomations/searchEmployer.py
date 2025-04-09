import requests
from bs4 import BeautifulSoup

def buscar_vagas(palavras_chave, localizacao):
    """Busca vagas de emprego em um site (exemplo simplificado)."""
    url = f"URL_DO_SITE_DE_VAGAS?q={palavras_chave}&l={localizacao}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    vagas = soup.find_all("div", class_="vaga")  # Substitua pelo seletor correto

    for vaga in vagas:
        titulo = vaga.find("h2").text.strip()
        descricao = vaga.find("p").text.strip()
        # Verifique se a vaga é compatível com seu perfil
        if "python" in descricao.lower() and "senior" in descricao.lower():
            print(f"Vaga encontrada: {titulo}")
            print(descricao)

buscar_vagas("desenvolvedor python", "sao paulo")