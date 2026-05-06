import random
import time
import curses

# Initialize the game window
def init_game():
    stdscr = curses.initscr()
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Window refresh rate
    height, width = stdscr.getmaxyx()  # Get window dimensions
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    return stdscr, win, height, width

# Define the game board
def create_board(height, width):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Create walls (use 'X' for walls)
    for i in range(width):
        board[0][i] = 'X'  # Top wall
        board[height-1][i] = 'X'  # Bottom wall
    for i in range(height):
        board[i][0] = 'X'  # Left wall
        board[i][width-1] = 'X'  # Right wall
    
    return board

# Function to display the game board
def print_board(win, board, pacman_pos, score):
    win.clear()
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if (y, x) == pacman_pos:
                win.addstr(y, x * 2, 'P', curses.color_pair(1))
            else:
                win.addstr(y, x * 2, row[x], curses.color_pair(0))
    
    win.addstr(0, 0, f"Score: {score}")
    win.refresh()

# Function to move Pac-Man
def move_pacman(pacman_pos, direction, board, height, width):
    y, x = pacman_pos
    if direction == 'UP' and y > 1 and board[y - 1][x] != 'X':
        return y - 1, x
    if direction == 'DOWN' and y < height - 2 and board[y + 1][x] != 'X':
        return y + 1, x
    if direction == 'LEFT' and x > 1 and board[y][x - 1] != 'X':
        return y, x - 1
    if direction == 'RIGHT' and x < width - 2 and board[y][x + 1] != 'X':
        return y, x + 1
    return pacman_pos

# Function to spawn dots ('.') on the board randomly
def spawn_dots(board, height, width, num_dots=10):
    for _ in range(num_dots):
        y = random.randint(1, height - 2)
        x = random.randint(1, width - 2)
        if board[y][x] == ' ':
            board[y][x] = '.'

# Main game loop
def game_loop(stdscr, win, height, width):
    pacman_pos = (height // 2, width // 2)  # Initial position of Pac-Man
    direction = 'RIGHT'
    score = 0
    board = create_board(height, width)
    spawn_dots(board, height, width)

    while True:
        key = win.getch()
        
        if key == 27:  # ESC key to quit
            break
        elif key == curses.KEY_UP:
            direction = 'UP'
        elif key == curses.KEY_DOWN:
            direction = 'DOWN'
        elif key == curses.KEY_LEFT:
            direction = 'LEFT'
        elif key == curses.KEY_RIGHT:
            direction = 'RIGHT'

        # Move Pac-Man
        new_pos = move_pacman(pacman_pos, direction, board, height, width)
        
        # Check if Pac-Man eats a dot
        if board[new_pos[0]][new_pos[1]] == '.':
            score += 10
            board[new_pos[0]][new_pos[1]] = ' '  # Remove the dot
        
        pacman_pos = new_pos

        # Print the updated board and score
        print_board(win, board, pacman_pos, score)

        # Spawn new dots as the game progresses
        if score % 50 == 0:  # Add new dots every 50 points
            spawn_dots(board, height, width)

        time.sleep(0.1)

# Start the game
def main():
    stdscr, win, height, width = init_game()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Yellow color for Pac-Man
    game_loop(stdscr, win, height, width)
    curses.endwin()  # End the window when the game is over

if __name__ == '__main__':
    main()