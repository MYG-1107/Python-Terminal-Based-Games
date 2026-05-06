import random
import os
import sys

# Directions
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
EXIT = 'q'

# Initial game board
size = 4

def print_board(board):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print("\nUse w, a, s, d to move. Press q to quit.\n")

def initialize_board():
    board = [[0] * size for _ in range(size)]
    add_random_number(board)
    add_random_number(board)
    return board

def add_random_number(board):
    empty_cells = [(r, c) for r in range(size) for c in range(size) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])

def move_left(row):
    new_row = [i for i in row if i != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0]
    return new_row + [0] * (size - len(new_row))

def rotate_board(board):
    return [list(x) for x in zip(*board)]

def move_board(board, direction):
    moved = False
    if direction == LEFT:
        for i in range(size):
            new_row = move_left(board[i])
            if new_row != board[i]:
                moved = True
            board[i] = new_row
    elif direction == RIGHT:
        for i in range(size):
            board[i] = list(reversed(board[i]))
            new_row = move_left(board[i])
            if new_row != board[i]:
                moved = True
            board[i] = list(reversed(new_row))
    elif direction == UP:
        board = rotate_board(board)
        moved = move_board(board, LEFT)
        board = rotate_board(board)
    elif direction == DOWN:
        board = rotate_board(board)
        moved = move_board(board, RIGHT)
        board = rotate_board(board)
    return moved, board

def check_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for r in range(size):
        for c in range(size - 1):
            if board[r][c] == board[r][c + 1]:
                return False
    for c in range(size):
        for r in range(size - 1):
            if board[r][c] == board[r + 1][c]:
                return False
    return True

def main():
    board = initialize_board()
    while True:
        print_board(board)
        direction = input("Enter direction (w/a/s/d) or q to quit: ").lower()
        if direction == EXIT:
            print("Goodbye!")
            break
        if direction not in [UP, DOWN, LEFT, RIGHT]:
            print("Invalid input! Please use w, a, s, d to move.")
            continue
        moved, board = move_board(board, direction)
        if moved:
            add_random_number(board)
        if check_game_over(board):
            print_board(board)
            print("Game Over!")
            break

if __name__ == "__main__":
    main()