# Tic-Tac-Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player):
        return True
    # Check columns
    if (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player):
        return True
    # Check diagonals
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        display_board()

        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player

            if check_winner(board, current_player):
                display_board()
                print("Player", current_player, "wins!")
                break
            elif is_board_full(board):
                display_board()
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
