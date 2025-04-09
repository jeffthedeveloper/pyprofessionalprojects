# Vamos criar uma função para exibir o tabuleiro no console.



def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro no console."""
    for i in range(0, 9, 3):
        print(tabuleiro[i], '|', tabuleiro[i+1], '|', tabuleiro[i+2])
        if i < 6:
            print('---------')