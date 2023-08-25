import random

# Função para embaralhar as peças de dominó
def embaralhar_domino():
    domino = []
    for i in range(7):
        for j in range(i, 7):
            domino.append((i, j))
    random.shuffle(domino)
    return domino

# Função para distribuir as peças para os jogadores
def distribuir_domino(dominos):
    player1 = dominos[:7]
    player2 = dominos[7:14]
    return player1, player2

# Função para imprimir as peças na mão do jogador
def mostrar_mao(mao_jogador):
    print("Suas peças:")
    for idx, domino in enumerate(mao_jogador, start=1):
        print(f"{idx}: {domino}")

# Função para verificar se uma jogada é válida
def jogo_valido(jogo, mesa):
    if not mesa:
        return True
    left_end, right_end = mesa[0], mesa[-1]
    return jogo[0] in (left_end[0], right_end[1]) or jogo[1] in (left_end[0], right_end[1])

# Função principal do jogo
def main():
    dominos = embaralhar_domino()
    mao_jogador1, mao_jogador2 = distribuir_domino(dominos)
    mesa = []

    jogador_atual = 1

    while True:
        if jogador_atual == 1:
            mao_jogador = mao_jogador1
        else:
            mao_jogador = mao_jogador2

        print("\n=======================")
        mostrar_mao(mao_jogador)
        print("Mesa:", mesa)

        jogo = int(input("Escolha o número da peça que deseja jogar (0 para pular): ")) - 1

        if jogo == -1:
            print("Você pulou a vez.")
        else:
            peca_escolhida = mao_jogador[jogo]
            if jogo_valido(peca_escolhida, mesa):
                mesa.append(peca_escolhida)
                mao_jogador.pop(jogo)
            else:
                print("Jogada inválida. Tente novamente.")

        if not mao_jogador:
            print(f"\nJogador {jogador_atual} venceu!")
            break

        jogador_atual = 3 - jogador_atual  # Alternar entre jogadores (1 <-> 2)

if __name__ == "__main__":
    main()
