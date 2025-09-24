## Simple Tic-Tac-Toe with Minimax + Alpha-Beta Pruning

import math

# Board setup
board = [" "] * 9
WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n")

def winner(b):
    for a,b1,c in WIN_LINES:
        if b[a] != " " and b[a] == b[b1] == b[c]:
            return b[a]
    return None

def available_moves(b):
    return [i for i,v in enumerate(b) if v==" "]

def minimax(b, depth, alpha, beta, isMax, ai, human):
    w = winner(b)
    if w == ai: return 1
    if w == human: return -1
    if " " not in b: return 0

    if isMax:  # AI's turn
        best = -math.inf
        for m in available_moves(b):
            b[m] = ai
            score = minimax(b, depth+1, alpha, beta, False, ai, human)
            b[m] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:  # Human's turn
        best = math.inf
        for m in available_moves(b):
            b[m] = human
            score = minimax(b, depth+1, alpha, beta, True, ai, human)
            b[m] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha: break
        return best

def best_move(b, ai, human):
    best_val, move = -math.inf, None
    for m in available_moves(b):
        b[m] = ai
        score = minimax(b, 0, -math.inf, math.inf, False, ai, human)
        b[m] = " "
        if score > best_val:
            best_val, move = score, m
    return move

# Game loop
human, ai = "O", "X"
turn = "human"

while True:
    print_board(board)
    if winner(board) or " " not in board:
        break

    if turn == "human":
        pos = int(input("Enter (1-9): ")) - 1
        if board[pos] == " ":
            board[pos] = human
            turn = "ai"
    else:
        pos = best_move(board, ai, human)
        board[pos] = ai
        print(f"AI chooses {pos+1}")
        turn = "human"

print_board(board)
w = winner(board)
print("Draw!" if not w else f"Winner: {w}")
