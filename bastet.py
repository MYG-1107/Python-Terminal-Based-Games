import random
import curses
import time

# Define the tetromino shapes
TETROMINOS = [
    [['#', '#', '#', '#']],  # I
    [['#', '#'], ['#', '#']],  # O
    [['#', '#', ' '], [' ', '#', '#']],  # S
    [[' ', '#', '#'], ['#', '#', ' ']],  # Z
    [['#', ' ', ' '], ['#', '#', '#']],  # L
    [[' ', ' ', '#'], ['#', '#', '#']],  # J
    [['#', '#', ' '], ['#', '#', ' ']],  # T
]

# Screen initialization
def init_game():
    stdscr = curses.initscr()
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Refresh every 100ms
    height, width = stdscr.getmaxyx()  # Get screen dimensions
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    return stdscr, win, height, width

# Function to rotate a tetromino
def rotate(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])]

# Function to check if a tetromino can be placed at a given position
def check_collision(board, tetromino, offset):
    off_x, off_y = offset
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            try:
                if cell != ' ' and board[y + off_y][x + off_x] != ' ':
                    return True
            except IndexError:
                return True
    return False

# Function to clear full lines
def clear_lines(board):
    new_board = [row for row in board if any(cell == ' ' for cell in row)]
    return [[' '] * len(board[0])] * (len(board) - len(new_board)) + new_board

# Function to generate a new random tetromino (Bastet style)
def generate_tetromino(board):
    # First, collect all valid tetrominoes that can fit
    valid_tetrominos = []
    for t in TETROMINOS:
        for _ in range(4):  # Rotate up to 4 times to check
            if not check_collision(board, t, (5, 0)):  # If it fits at the top middle
                valid_tetrominos.append(t)
            t = rotate(t)
    
    # Return a random "frustrating" tetromino (the one that's the least likely to fit)
    if valid_tetrominos:
        return random.choice(valid_tetrominos)
    else:
        return TETROMINOS[0]  # If no valid block, return the first one

# Function to display the board
def display_board(win, board):
    win.clear()
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            win.addstr(y, x * 2, cell)  # Display each block, space between them
    win.refresh()

# Main game loop
def game_loop(stdscr, win, height, width):
    board = [[' '] * (width // 2) for _ in range(height - 1)]  # Tetris grid (height - 1 because of bottom)
    tetromino = generate_tetromino(board)
    tetromino_x = width // 4
    tetromino_y = 0
    score = 0

    while True:
        key = win.getch()
        if key == 27:  # ESC to quit
            break

        # Move or rotate the tetromino
        if key == curses.KEY_RIGHT:
            if not check_collision(board, tetromino, (tetromino_x + 1, tetromino_y)):
                tetromino_x += 1
        elif key == curses.KEY_LEFT:
            if not check_collision(board, tetromino, (tetromino_x - 1, tetromino_y)):
                tetromino_x -= 1
        elif key == curses.KEY_DOWN:
            if not check_collision(board, tetromino, (tetromino_x, tetromino_y + 1)):
                tetromino_y += 1
            else:
                # Place the tetromino when it hits the ground
                for y, row in enumerate(tetromino):
                    for x, cell in enumerate(row):
                        if cell != ' ':
                            board[y + tetromino_y][x + tetromino_x] = cell
                board = clear_lines(board)
                tetromino = generate_tetromino(board)
                tetromino_x = width // 4
                tetromino_y = 0
                score += 10  # Increase score for clearing a line

        elif key == ord(' '):  # Space to rotate
            new_tetromino = rotate(tetromino)
            if not check_collision(board, new_tetromino, (tetromino_x, tetromino_y)):
                tetromino = new_tetromino

        # Display board and score
        display_board(win, board)
        win.addstr(0, width // 2 - 5, f"Score: {score}")

        # Check for game over (if new tetromino cannot be placed)
        if check_collision(board, tetromino, (tetromino_x, tetromino_y)):
            break

        time.sleep(0.05)

# Start the game
def main():
    stdscr, win, height, width = init_game()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Block color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Score color
    game_loop(stdscr, win, height, width)
    curses.endwin()

if __name__ == '__main__':
    main()