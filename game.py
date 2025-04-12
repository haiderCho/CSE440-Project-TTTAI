from ai import minimax
import math

def print_board(board):

    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")

def player_move(board, human_player):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = human_player
                break
            else:
                print("Invalid move. The cell is already occupied or out of range. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board, ai_player, use_heuristic=False):
    print("AI is thinking...")
    _, move = minimax(board, depth=9, alpha=-math.inf, beta=math.inf, maximizing=True, player=ai_player, use_heuristic=use_heuristic)
    if move is not None:
        board[move] = ai_player