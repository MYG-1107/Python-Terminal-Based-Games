# Import necessary libraries
import random
import sys

# ==============================
# 1. Word Chain Game
# ==============================
def word_chain_game(user_name):
    """
    A game where players take turns to say a word that starts with the last letter of the previous word.
    """
    print(f"Welcome to Word Chain Game, {user_name}!")
    previous_word = input("Enter the starting word: ").strip().lower()
    used_words = [previous_word]

    while True:
        next_word = input(f"Your word must start with '{previous_word[-1]}' (or type 'quit' to exit): ").strip().lower()
        if next_word == "quit":
            print(f"Thanks for playing, {user_name}! Returning to the main menu.")
            break
        if next_word in used_words:
            print("Word already used! Try again.")
        elif next_word[0] != previous_word[-1]:
            print(f"Word must start with '{previous_word[-1]}'! Try again.")
        else:
            used_words.append(next_word)
            previous_word = next_word

# ==============================
# 2. Hangman Game
# ==============================
def hangman_game(user_name):
    """
    A classic hangman game where the player guesses letters to complete a hidden word.
    """
    print(f"Welcome to Hangman, {user_name}!")
    words = ["python", "programming", "hangman", "challenge", "developer"]
    word = random.choice(words)
    guessed = "_" * len(word)
    guessed = list(guessed)
    attempts = 6
    guessed_letters = []

    while attempts > 0 and "_" in guessed:
        print("\nWord: " + " ".join(guessed))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter (or type 'quit' to exit): ").lower()

        if guess == "quit":
            print(f"Thanks for playing, {user_name}! Returning to the main menu.")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word: " + "".join(guessed))
    else:
        print("\nYou lost! The word was: " + word)

# ==============================
# 3. Tic-Tac-Toe Game (with AI and Two-Player Mode)
# ==============================
def print_board(board):
    """Helper function to print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Helper function to check if a player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Helper function to check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe_ai_move(board):
    """Simple AI move for Tic-Tac-Toe."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col
    return None

def tic_tac_toe_game(user_name):
    """
    Tic-Tac-Toe game with two-player mode and a simple AI.
    """
    print(f"Welcome to Tic-Tac-Toe, {user_name}!")
    mode = input("Choose mode (1 for Two-Player, 2 for vs AI): ").strip()
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if mode == "1" or (mode == "2" and current_player == "X"):
            move = input(f"Player {current_player}, enter row and column (0-2) or type 'quit' to exit: ").strip()
            if move == "quit":
                print(f"Thanks for playing, {user_name}! Returning to the main menu.")
                return
            row, col = map(int, move.split())
        else:
            print("AI is making a move...")
            row, col = tic_tac_toe_ai_move(board)

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# ==============================
# 4. Word Guessing Game
# ==============================
def word_guessing_game(user_name):
    """
    A game where the player guesses a word based on hints.
    """
    print(f"Welcome to Word Guessing Game, {user_name}!")
    words = {"variable": "A named storage location that holds a value.", "function": "A reusable block of code that performs a specific task.",}
    word, hint = random.choice(list(words.items()))
    guessed = "_" * len(word)
    guessed = list(guessed)
    attempts = 5

    while attempts > 0 and "_" in guessed:
        print("\nWord: " + " ".join(guessed))
        print(f"Hint: {hint}")
        guess = input("Guess a letter or the whole word (or type 'quit' to exit): ").lower()

        if guess == "quit":
            print(f"Thanks for playing, {user_name}! Returning to the main menu.")
            return

        if len(guess) == 1:
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed[i] = guess
            else:
                attempts -= 1
                print(f"Wrong guess! Attempts left: {attempts}")
        else:
            if guess == word:
                print("Congratulations! You guessed the word!")
                return
            else:
                attempts -= 1
                print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word: " + "".join(guessed))
    else:
        print("\nYou lost! The word was: " + word)

# ==============================
# 5. Number Guessing Game
# ==============================
def number_guessing_game(user_name):
    """
    A game where the player guesses a randomly generated number.
    """
    print(f"Welcome to Number Guessing Game, {user_name}!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100 (or type 'quit' to exit): ").strip()
        if guess == "quit":
            print(f"Thanks for playing, {user_name}! Returning to the main menu.")
            return

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# ==============================
# 6. Text-Based Adventure Game
# ==============================
def text_adventure_game(user_name):
    """
    A simple text-based adventure game with multiple choices.
    """
    print(f"Welcome to Text-Based Adventure Game, {user_name}!")
    print("You are in a dark forest. You can go 'left' or 'right'.")
    choice = input("Which way do you want to go? (or type 'quit' to exit): ").strip().lower()

    if choice == "quit":
        print(f"Thanks for playing, {user_name}! Returning to the main menu.")
        return
    elif choice == "left":
        print("You found a treasure chest! You win!")
    elif choice == "right":
        print("You fell into a pit. Game over!")
    else:
        print("Invalid choice. Game over!")

# ==============================
# 7. Madlibs Game
# ==============================
def madlibs_game(user_name):
    """
    A game where the player fills in blanks to create a funny story.
    """
    print(f"Welcome to Madlibs, {user_name}!")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    story = f"Once upon a time, a {adjective} {noun} decided to {verb} all the way to {place}. It was a wild adventure!"
    print("\nYour Madlibs Story:\n" + story)

# ==============================
# Main Menu
# ==============================
def main():
    """
    Main menu to select and play the games.
    """
    # Ask for the user's name
    user_name = input("Enter your name: ").strip()
    print(f"Welcome, {user_name}!")

    games = {
        "1": ("Word Chain Game", word_chain_game),
        "2": ("Hangman Game", hangman_game),
        "3": ("Tic-Tac-Toe Game", tic_tac_toe_game),
        "4": ("Word Guessing Game", word_guessing_game),
        "5": ("Number Guessing Game", number_guessing_game),
        "6": ("Text-Based Adventure Game", text_adventure_game),
        "7": ("Madlibs Game", madlibs_game),
    }

    while True:
        print("\n===== Interactive Python-Based Terminal Gaming System =====")
        for key, (name, _) in games.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Select a game (1-7) or 0 to exit: ").strip()

        if choice == "0":
            print(f"Thank you for playing, {user_name}! Goodbye!")
            break
        elif choice in games:
            games[choice][1](user_name)  # Pass the user's name to the game function
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()