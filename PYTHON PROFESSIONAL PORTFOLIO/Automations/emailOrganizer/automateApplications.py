from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def aplicar_vaga(url_vaga, caminho_curriculo):
    """Automatiza a aplicação para uma vaga (exige adaptação para cada site)."""
    driver = webdriver.Chrome()
    driver.get(url_vaga)
    # Adapte esses seletores para o site de vagas específico
    driver.find_element(By.ID, "botao_aplicar").click()
    driver.find_element(By.ID, "campo_curriculo").send_keys(caminho_curriculo)
    driver.find_element(By.ID, "botao_enviar").click()
    time.sleep(5)
    driver.quit()

aplicar_vaga("URL_DA_VAGA", "caminho/para/seu/curriculo.pdf")