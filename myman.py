import curses
import random
import time

# Define characters
PACMAN = "P"
GHOST = "G"
DOT = "."
WALL = "#"
EMPTY = " "

# Maze Layout
maze_layout = [
    "####################",
    "#P.......#........#",
    "#.#####.#.#.#####.#",
    "#.................#",
    "#.#####.#.#.#####.#",
    "#........#........#",
    "####################"
]

# Convert maze to list of lists
def create_maze():
    return [list(row) for row in maze_layout]

# Get positions of specific characters in the maze
def get_positions(maze, char):
    positions = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == char:
                positions.append((y, x))
    return positions

# Main game loop
def myman(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(200)  # Game speed

    high_score = 0

    while True:  # Loop for replaying the game
        maze = create_maze()  # Reset maze for new game
        pacman_pos = get_positions(maze, PACMAN)[0]
        ghost_pos = get_positions(maze, DOT)[0]  # Randomly place ghost on a dot
        score = 0
        direction = (0, 0)

        # Display instructions
        stdscr.clear()
        stdscr.addstr(1, 5, "🎮 Welcome to MyMan (Pac-Man for Console) 🎮")
        stdscr.addstr(3, 2, "Controls:")
        stdscr.addstr(4, 2, "➡ Arrow Keys: Move Pac-Man")
        stdscr.addstr(5, 2, "❌ Q or ESC: Quit Game")
        stdscr.addstr(7, 2, "🍒 Eat all dots (.) to win!")
        stdscr.addstr(8, 2, "👻 Avoid the ghost (G)!")
        stdscr.addstr(10, 2, "Press any key to start...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to start

        # Game loop
        game_over = False
        while not game_over:
            stdscr.clear()

            # Draw the maze
            for y, row in enumerate(maze):
                stdscr.addstr(y, 0, "".join(row))

            # Move Pac-Man
            new_y, new_x = pacman_pos[0] + direction[0], pacman_pos[1] + direction[1]
            if maze[new_y][new_x] in (EMPTY, DOT):
                if maze[new_y][new_x] == DOT:
                    score += 10  # Increase score for eating a dot
                maze[pacman_pos[0]][pacman_pos[1]] = EMPTY
                pacman_pos = (new_y, new_x)
                maze[new_y][new_x] = PACMAN  # Move Pac-Man

            # Move Ghost randomly
            ghost_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(ghost_moves)
            for dy, dx in ghost_moves:
                new_gy, new_gx = ghost_pos[0] + dy, ghost_pos[1] + dx
                if maze[new_gy][new_gx] in (EMPTY, DOT):
                    maze[ghost_pos[0]][ghost_pos[1]] = EMPTY  # Clear old position
                    ghost_pos = (new_gy, new_gx)
                    maze[new_gy][new_gx] = GHOST  # Move Ghost
                    break

            # Display Score
            stdscr.addstr(len(maze), 0, f"Score: {score}  |  High Score: {high_score}")

            # Check if game is over (Pac-Man caught)
            if pacman_pos == ghost_pos:
                stdscr.addstr(len(maze) + 1, 0, "💀 Game Over! Pac-Man was caught! 💀")
                game_over = True

            # Check if all dots are eaten (Win condition)
            remaining_dots = sum(row.count(DOT) for row in maze)
            if remaining_dots == 0:
                stdscr.addstr(len(maze) + 1, 0, "🎉 Congratulations! You ate all the dots! 🎉")
                game_over = True

            # Get user input
            key = stdscr.getch()
            if key in [ord("q"), 27]:  # Quit game on 'q' or ESC
                return  # Exit the game
            elif key == curses.KEY_UP:
                direction = (-1, 0)
            elif key == curses.KEY_DOWN:
                direction = (1, 0)
            elif key == curses.KEY_LEFT:
                direction = (0, -1)
            elif key == curses.KEY_RIGHT:
                direction = (0, 1)

            stdscr.refresh()

        # Check and update high score
        if score > high_score:
            high_score = score
            stdscr.addstr(len(maze) + 2, 0, f"🏆 New High Score: {high_score} 🏆")
        else:
            stdscr.addstr(len(maze) + 2, 0, f"🥇 Highest Score so far: {high_score}")

        # Ask if player wants to play again
        stdscr.addstr(len(maze) + 4, 0, "🔁 Play Again? (Y/N) ")
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key in [ord("y"), ord("Y")]:
                break  # Restart game loop
            elif key in [ord("n"), ord("N"), ord("q"), 27]:
                return  # Exit the game
# Run the game
curses.wrapper(myman)