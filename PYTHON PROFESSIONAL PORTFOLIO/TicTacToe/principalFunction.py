def jogo_da_velha():
    """Função principal do jogo."""
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