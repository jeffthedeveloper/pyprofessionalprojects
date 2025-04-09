import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

def adicionar_marca_dagua():
    """Adiciona uma marca d'água a uma imagem."""
    imagem_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if not imagem_path:
        return

    marca_dagua_texto = marca_dagua_entry.get()
    if not marca_dagua_texto:
        messagebox.showerror("Erro", "Digite a marca d'água.")
        return

    try:
        imagem = Image.open(imagem_path).convert("RGBA")
        largura, altura = imagem.size

        draw = ImageDraw.Draw(imagem)
        fonte = ImageFont.truetype("arial.ttf", 36)  # Escolha uma fonte e tamanho
        texto_largura, texto_altura = draw.textsize(marca_dagua_texto, font=fonte)

        posicao = (largura - texto_largura - 10, altura - texto_altura - 10)  # Posição no canto inferior direito
        draw.text(posicao, marca_dagua_texto, font=fonte, fill=(255, 255, 255, 128))  # Cor e opacidade

        salvar_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagens PNG", "*.png")])
        if salvar_path:
            imagem.save(salvar_path)
            messagebox.showinfo("Sucesso", "Marca d'água adicionada com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Interface gráfica
janela = tk.Tk()
janela.title("Adicionar Marca d'água")

marca_dagua_label = tk.Label(janela, text="Marca d'água:")
marca_dagua_label.pack()

marca_dagua_entry = tk.Entry(janela)
marca_dagua_entry.pack()

adicionar_botao = tk.Button(janela, text="Adicionar Marca d'água", command=adicionar_marca_dagua)
adicionar_botao.pack()

janela.mainloop()