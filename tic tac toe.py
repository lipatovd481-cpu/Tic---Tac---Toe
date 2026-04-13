board = [" " for _ in range(9)]


def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def print_hint():
    print()
    print("1 | 2 | 3")
    print("---+---+---")
    print("4 | 5 | 6")
    print("---+---+---")
    print("7 | 8 | 9")
    print()


def check_win(player):
    win_positions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]

    for pos in win_positions:
        if (
            board[pos[0]] == player
            and board[pos[1]] == player
            and board[pos[2]] == player
        ):
            return True
    return False


def is_draw():
    return "" not in board


def make_move(player):
    while True:
        move = input(f"Ход игрока {player}. Выбереите клетку (1 - 9):")
        if not move.isdigit():
            print("Введите число от 1 до 9.")
            continue
        index = move - 1
        if board[index] != "":
            print("Эта клетка занята.")
            continue

        board[index] = player
        break

    def play_game():
        current_player = "X"

        print("Игра крестики - нолики")
        print_hint()

        while True:
            print_board()
            make_move(current_player)

            if check_win(current_player):
                print_board()
                print(f"Игрок {current_player} победил!")
                break

            if is_draw():
                print_board()
                print("Ничья!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

    play_game()
