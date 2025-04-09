def criar_tabuleiro():
    return [' '] * 9

def exibir_tabuleiro(tabuleiro):
    for i in range(0, 9, 3):
        print(tabuleiro[i], '|', tabuleiro[i+1], '|', tabuleiro[i+2])
        if i < 6:
            print('---------')

def verificar_vitoria(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def jogada_jogador(tabuleiro, jogador):
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

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)
        jogada_jogador(tabuleiro, jogador_atual)

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogo_da_velha()