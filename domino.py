import random

# Função para embaralhar as peças de dominó
def shuffle_dominoes():
    dominos = []
    for i in range(7):
        for j in range(i, 7):
            dominos.append((i, j))
    random.shuffle(dominos)
    return dominos

# Função para distribuir as peças para os jogadores
def deal_dominoes(dominos):
    player1_hand = dominos[:7]
    player2_hand = dominos[7:14]
    return player1_hand, player2_hand

# Função para imprimir as peças na mão do jogador
def print_hand(player_hand):
    print("Suas peças:")
    for idx, domino in enumerate(player_hand, start=1):
        print(f"{idx}: {domino}")

# Função para verificar se uma jogada é válida
def is_valid_play(play, table):
    if not table:
        return True
    left_end, right_end = table[0], table[-1]
    return play[0] in (left_end[0], right_end[1]) or play[1] in (left_end[0], right_end[1])

# Função principal do jogo
def main():
    dominos = shuffle_dominoes()
    player1_hand, player2_hand = deal_dominoes(dominos)
    table = []

    current_player = 1

    while True:
        if current_player == 1:
            player_hand = player1_hand
        else:
            player_hand = player2_hand

        print("\n=======================")
        print_hand(player_hand)
        print("Mesa:", table)

        play_index = int(input("Escolha o número da peça que deseja jogar (0 para pular): ")) - 1

        if play_index == -1:
            print("Você pulou a vez.")
        else:
            chosen_play = player_hand[play_index]
            if is_valid_play(chosen_play, table):
                table.append(chosen_play)
                player_hand.pop(play_index)
            else:
                print("Jogada inválida. Tente novamente.")

        if not player_hand:
            print(f"\nJogador {current_player} venceu!")
            break

        current_player = 3 - current_player  # Alternar entre jogadores (1 <-> 2)

if __name__ == "__main__":
    main()
