import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_board(difficulty):
    base_board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(difficulty * 5):
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid(base_board, row, col, num) or base_board[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        base_board[row][col] = num
    return base_board

def get_difficulty_level():
    print("Select Difficulty Level: (1) Easy (2) Medium (3) Hard")
    choice = input("Enter 1, 2, or 3: ")
    return int(choice)

def main():
    difficulty = get_difficulty_level()
    print("Generating puzzle...")
    board = generate_board(difficulty)
    print("Here is your Sudoku puzzle!")
    print_board(board)
    
    while True:
        row, col, num = map(int, input("Enter row, column (1-9), and number (1-9): ").split())
        if row < 1 or row > 9 or col < 1 or col > 9 or num < 1 or num > 9:
            print("Invalid input! Please enter numbers between 1 and 9.")
            continue
        row, col = row - 1, col - 1  # Adjusting to 0-based index
        if not is_valid(board, row, col, num):
            print("Invalid move! Try again.")
        else:
            board[row][col] = num
            print_board(board)
            if all(board[row][col] != 0 for row in range(9) for col in range(9)):
                print("Congratulations! You've solved the puzzle!")
                break

if __name__ == "__main__":
    main()
