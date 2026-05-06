import random
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

# Function to display the game board
def display_board(win, snake, food, score):
    win.clear()
    height, width = win.getmaxyx()

    # Print score
    win.addstr(0, 2, f"Score: {score}")

    # Print snake
    for y, x in snake:
        win.addstr(y, x, '■', curses.color_pair(1))

    # Print food
    fy, fx = food
    win.addstr(fy, fx, '■', curses.color_pair(2))

    win.refresh()

# Function to move the snake
def move_snake(snake, direction, height, width):
    head_y, head_x = snake[0]
    if direction == curses.KEY_UP:
        new_head = (head_y - 1, head_x)
    elif direction == curses.KEY_DOWN:
        new_head = (head_y + 1, head_x)
    elif direction == curses.KEY_LEFT:
        new_head = (head_y, head_x - 1)
    elif direction == curses.KEY_RIGHT:
        new_head = (head_y, head_x + 1)

    # Insert the new head at the beginning of the snake list
    snake.insert(0, new_head)

    # Check if snake hits wall or itself
    if new_head[0] in [0, height] or new_head[1] in [0, width] or new_head in snake[1:]:
        return True  # Game over

    return False

# Function to generate food at a random location
def generate_food(snake, height, width):
    while True:
        food = (random.randint(1, height - 2), random.randint(1, width - 2))
        if food not in snake:
            return food

# Main game loop
def game_loop(stdscr, win, height, width):
    snake = [(height // 2, width // 4), (height // 2, width // 4 - 1), (height // 2, width // 4 - 2)]  # Snake starting position
    direction = curses.KEY_RIGHT
    score = 0
    food = generate_food(snake, height, width)

    while True:
        key = win.getch()
        if key == 27:  # ESC key to quit
            break
        elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key

        # Move snake
        game_over = move_snake(snake, direction, height, width)

        # Check if snake ate food
        if snake[0] == food:
            score += 10
            food = generate_food(snake, height, width)
        else:
            snake.pop()  # Remove the tail

        # Display the updated game board
        display_board(win, snake, food, score)

        # If the game is over, break the loop
        if game_over:
            break

# Start the game
def main():
    stdscr, win, height, width = init_game()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Food color
    game_loop(stdscr, win, height, width)
    curses.endwin()  # End the window when the game is over

if __name__ == '__main__':
    main()
