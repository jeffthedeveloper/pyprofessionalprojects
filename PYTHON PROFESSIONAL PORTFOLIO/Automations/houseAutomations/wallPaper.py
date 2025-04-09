import requests
import os
import ctypes

def obter_imagem_nasa():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url).json()
    image_url = response["url"]
    response = requests.get(image_url)
    with open("nasa_image.jpg", "wb") as f:
        f.write(response.content)
    return "nasa_image.jpg"

def definir_papel_parede(caminho_imagem):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, caminho_imagem, 3) # para windows
# Para linux use a biblioteca os e o comando gsettings

caminho = obter_imagem_nasa()
definir_papel_parede(caminho)