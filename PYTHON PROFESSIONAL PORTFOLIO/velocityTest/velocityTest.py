import tkinter as tk
import time
import random

TEXTOS = [
    "A rápida raposa marrom pula sobre o cão preguiçoso.",
    "Programar em Python é divertido e desafiador.",
    "O sol brilha forte em um dia de verão.",
    "A persistência leva ao sucesso.",
    "A criatividade é a chave para a inovação."
]

def iniciar_teste():
    """Inicia o teste de digitação."""
    global texto_atual, tempo_inicio
    texto_atual = random.choice(TEXTOS)
    texto_label.config(text=texto_atual)
    entrada_texto.delete(0, tk.END)
    tempo_inicio = time.time()
    iniciar_botao.config(state=tk.DISABLED)
    entrada_texto.config(state=tk.NORMAL)
    entrada_texto.focus_set()

def finalizar_teste(event=None):
    """Finaliza o teste e calcula a velocidade de digitação."""
    global tempo_inicio
    tempo_fim = time.time()
    tempo_total = tempo_fim - tempo_inicio
    texto_digitado = entrada_texto.get()
    palavras_digitadas = len(texto_digitado.split())
    velocidade = int(palavras_digitadas / (tempo_total / 60))
    resultado_label.config(text=f"Sua velocidade: {velocidade} palavras por minuto (PPM)")
    iniciar_botao.config(state=tk.NORMAL)
    entrada_texto.config(state=tk.DISABLED)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Teste de Velocidade de Digitação")

# Widgets
texto_label = tk.Label(janela, text="", wraplength=400)
texto_label.pack(pady=20)

entrada_texto = tk.Entry(janela, state=tk.DISABLED)
entrada_texto.pack(pady=10)
entrada_texto.bind('<Return>', finalizar_teste)

iniciar_botao = tk.Button(janela, text="Iniciar Teste", command=iniciar_teste)
iniciar_botao.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=20)

# Variáveis globais
texto_atual = ""
tempo_inicio = 0

# Loop principal
janela.mainloop()