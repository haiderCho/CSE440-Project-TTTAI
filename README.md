<h1 align="center"> CSE440 (Artificial Intelligence): Project </h1>
<h2 align="center">  Tic-Tac-Toe: AI with Minimax & Alpha-Beta Pruning
<p align="center">
 <img alt="Languages" src="https://img.shields.io/github/languages/count/haiderCho/CSE440-Project-TTTAI">
 <img alt="Repository size" src="https://img.shields.io/github/repo-size/haiderCho/CSE440-Project-TTTAI">
 <img alt="Contributors" src="https://img.shields.io/github/contributors/haiderCho/CSE440-Project-TTTAI">
 <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/haiderCho/CSE440-Project-TTTAI">
</p>
</h2>

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A command-line Tic-Tac-Toe game where you play against an unbeatable AI powered by the Minimax algorithm with optional heuristic evaluation for faster performance.

![tic-tac-toe-banner](https://upload.wikimedia.org/wikipedia/commons/3/32/Tic_tac_toe.svg)


## 🧠 Features

- Human vs AI gameplay
- Minimax algorithm with alpha-beta pruning
- Optional heuristic evaluation for faster decision-making
- Command-line interface (CLI)
- Modular and clean code structure


## 📦 Project Structure

```
project/
│
├── main.py
├── support/
│   ├── __init__.py
│   ├── game.py
│   └── ai.py
````
### `main.py`
- Manages game flow and user interaction.
- Prompts user to choose a side (`X` or `O`).
- Allows enabling or disabling heuristic-based AI moves.

### `support/game.py`
- `print_board(board)`: Nicely formats and prints the current board.
- `player_move(board, human_player)`: Accepts validated player input.
- `ai_move(board, ai_player, use_heuristic=False)`: Makes a move using minimax or heuristic strategy.

### `support/ai.py`
- `check_winner(board)`: Checks for win or draw conditions.
- `heuristic(board, player)`: Evaluates board for potential gains/losses.
- `minimax(...)`: AI decision-making with optional heuristic shortcut.


## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai
````

### 2. Run the game

```bash
python main.py
```


## 🕹️ How to Play

- You'll be asked to choose a side: `X` or `O`.
- The board is displayed using positions `1-9` as reference.
- On your turn, enter a number from 1 to 9 to place your move.
- The AI uses the Minimax algorithm to play optimally.


## ⚙️ Heuristic Mode (Optional)

If you'd like the AI to use a heuristic (faster decisions with slightly less accuracy), you’ll be prompted at the beginning of the game:

```
Limit search depth using a heuristic evaluation? (y/n): y
```
- Choose **`y`** to enable heuristic-based evaluation at limited depth — this makes the AI faster (helpful in large search spaces).
- Choose **`n`** to let the AI perform full-depth minimax (slower but perfect play). 


## 📚 Requirements

- Python 3.6+
- No third-party libraries required (uses only the Python standard library)

    ## 🧪 Sample Board Position Reference

```text
Board positions:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

This guide will help you enter your move on the correct tile.


## 📈 Future Improvements

- GUI version (using `pygame` or `tkinter`)
- Online multiplayer mode
- Score tracking
- Difficulty levels

