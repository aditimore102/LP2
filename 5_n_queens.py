def is_safe(board, row, col, n):
    # Check if queen can be placed at board[row][col]
    
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):  # Branch and Bound check
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1, n):  # Recursive backtracking
                return True
            board[row][col] = 0  # Backtrack (remove queen)

    return False

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] == 1 else '.', end=" ")
        print()
        
if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print("\nOne solution to the", n, "Queens problem:")
        print_board(board, n)
    else:
        print("\nNo solution exists!")
