""" Lógica do jogo:

Verificar vitória: Vamos criar uma função para verificar se um jogador venceu.
Verificar empate: Vamos criar uma função para verificar se o jogo terminou em empate.
Jogada do jogador: Vamos criar uma função para obter a jogada do jogador.
Jogada do computador (opcional): Se você quiser adicionar um oponente computadorizado, pode criar uma função para a jogada do computador. """

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se um jogador venceu."""
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate."""
    return ' ' not in tabuleiro

def jogada_jogador(tabuleiro, jogador):
    """Obtém a jogada do jogador."""
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
            if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador
                return
            else:
                print("Posição inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")