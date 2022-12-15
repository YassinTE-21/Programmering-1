# This is a simple implementation of the 4-in-a-row game using Python
# The game board is represented as a 2D list of integers, where 0 represents an empty cell
# and 1 or 2 represent the player's pieces on the board

# Define the dimensions of the game board
BOARD_ROWS = 6
BOARD_COLS = 7

# Create the game board as a 2D list of zeros
board = [[0 for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]

# Define the player who is currently making a move
current_player = 1

# Define a function to print the game board to the screen
def print_board(board):
    for row in board:
        print(" ".join([str(cell) for cell in row]))


# Define a function to check if the current player has won the game
def check_win(board, current_player):
    # Check for horizontal wins
    for row in board:
        for col in range(BOARD_COLS - 3):
            if (
                row[col] == current_player
                and row[col + 1] == current_player
                and row[col + 2] == current_player
                and row[col + 3] == current_player
            ):
                return True

    # Check for vertical wins
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if (
                board[row][col] == current_player
                and board[row + 1][col] == current_player
                and board[row + 2][col] == current_player
                and board[row + 3][col] == current_player
            ):
                return True

    # Check for diagonal wins (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if (
                board[row][col] == current_player
                and board[row + 1][col + 1] == current_player
                and board[row + 2][col + 2] == current_player
                and board[row + 3][col + 3] == current_player
            ):
                return True

    # Check for diagonal wins (top-right to bottom-left)
    for row in range(BOARD_ROWS - 3):
        for col in range(3, BOARD_COLS):
            if (
                board[row][col] == current_player
                and board[row + 1][col - 1] == current_player
                and board[row + 2][col - 2] == current_player
                and board[row + 3][col - 3] == current_player
            ):
                return True

    # If none of the above checks are true, then the player has not won
    return False


# Define a function to make a move for the current player
def make_move(board, current_player, col):
    # Check if the column is full
    if board[0][col] != 0:
        print("Column is full! Try again.")
        return

    # Place the player's piece in the first empty cell in the chosen column
