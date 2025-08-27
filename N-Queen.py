def solveNQueens(n):
    board = [-1] * n   # board[i] = column of queen in row i
    solutions = []

    def safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):  # same column or diagonal
                return False
        return True

    def place(row):
        if row == n:  # solution found
            sol = []
            for r in range(n):
                line = "." * board[r] + "Q" + "." * (n - board[r] - 1)
                sol.append(line)
            solutions.append(sol)
            return
        for col in range(n):
            if safe(row, col):
                board[row] = col
                place(row + 1)

    place(0)
    return solutions


# Example
N = 4
ans = solveNQueens(N)
print(f"Total solutions for {N}-Queens: {len(ans)}\n")
for sol in ans:
    for row in sol:
        print(row)
    print()