import math

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] != " " and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

def heuristic(board, player):
    opponent = "O" if player == "X" else "X"
    score = 0
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in lines:
        line_values = [board[i] for i in line]
        if line_values.count(player) == 2 and line_values.count(" ") == 1:
            score += 10
        elif line_values.count(player) == 1 and line_values.count(" ") == 2:
            score += 1
        if line_values.count(opponent) == 2 and line_values.count(" ") == 1:
            score -= 8
    return score

def minimax(board, depth, alpha, beta, maximizing, player, use_heuristic=False):

    result = check_winner(board)
    if result is not None:
        if result == "Draw":
            return 0, None
        return (1e6 if result == player else -1e6), None

    if depth == 0 and use_heuristic:
        return heuristic(board, player), None

    if maximizing:
        max_eval = -math.inf
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                eval, _ = minimax(board, depth - 1, alpha, beta, False, player, use_heuristic)
                board[i] = " "
                if eval > max_eval:
                    max_eval = eval
                    best_move = i
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        opponent = "O" if player == "X" else "X"
        for i in range(9):
            if board[i] == " ":
                board[i] = opponent
                eval, _ = minimax(board, depth - 1, alpha, beta, True, player, use_heuristic)
                board[i] = " "
                if eval < min_eval:
                    min_eval = eval
                    best_move = i
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move