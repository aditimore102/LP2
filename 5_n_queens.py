# ----------------------------
# Helper Function: Check if it's safe to place a queen
# ----------------------------
def is_safe(board, row, col, n):
    # Check vertically above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left upper diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right upper diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  # No conflicts, safe to place queen

# ----------------------------
# Recursive Function to Solve N-Queens
# ----------------------------
def solve_n_queens(board, row, n):
    # Base case: All queens placed
    if row == n:
        return True

    # Try placing queen in each column of this row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            if solve_n_queens(board, row + 1, n):  # Recurse to next row
                return True

            board[row][col] = 0  # Backtrack: Remove queen if not a solution

    return False  # No valid position in this row

# ----------------------------
# Print the Board Nicely
# ----------------------------
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] == 1 else '.', end=" ")
        print()

# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))
    
    # Initialize empty board (n x n) with 0s
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the problem
    if solve_n_queens(board, 0, n):
        print("\nOne solution to the", n, "Queens problem:")
        print_board(board, n)
    else:
        print("\nNo solution exists!")
