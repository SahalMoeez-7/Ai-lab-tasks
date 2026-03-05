
# Tic Tac Toe Game (2 Player Version)

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def play_game():
    board = [" "] * 9
    current_player = "X"
    move_count = 0

    print("\nPositions:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")

    while True:
        print_board(board)

        try:
            position = int(input(f"Player {current_player}, enter position (0-8): "))

            if position < 0 or position > 8:
                print("Invalid position!")
                continue

            if board[position] != " ":
                print("Position already taken!")
                continue

            board[position] = current_player
            move_count += 1

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if move_count == 9:
                print_board(board)
                print("It's a Draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Enter a valid number!")


if __name__ == "__main__":
    play_game()
```
