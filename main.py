from support.game import print_board, ai_move, player_move
from support.ai import check_winner

def main():
    # Initialize an empty Tic Tac Toe board
    board = [" "] * 9
    human_player = ""
    ai_player = ""

    # Ask the player to choose a side
    while human_player not in ["X", "O"]:
        human_player = input("Choose your side (X/O): ").upper()

    ai_player = "O" if human_player == "X" else "X"
    current_player = "X"  # X always starts first

    # Show the numbered board layout
    print("\nBoard positions:")
    print(" 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9\n")
    print("Game start!\n")

  
