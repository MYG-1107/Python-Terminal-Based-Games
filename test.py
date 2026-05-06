import random
import re

def word_chain():
    """Word Chain Game"""
    print("\nWelcome to Word Chain!")
    words = set()
    prev_word = input("Enter the first word: ").strip().lower()
    words.add(prev_word)
    
    while True:
        next_word = input(f"Enter a word starting with '{prev_word[-1]}': ").strip().lower()
        if next_word in words or not next_word.startswith(prev_word[-1]):
            print("Invalid word. Game over!")
            break
        words.add(next_word)
        prev_word = next_word


def hangman():
    """Hangman Game"""
    words = ["python", "developer", "terminal", "gaming", "engagement"]
    word = random.choice(words)
    guessed = set()
    attempts = 6
    display = ['_' for _ in word]
    
    print("\nWelcome to Hangman!")
    while attempts > 0 and '_' in display:
        print("Word: ", ' '.join(display))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = letter
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
        
        guessed.add(guess)
    
    if '_' not in display:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was {word}.")


def tic_tac_toe():
    """Tic-Tac-Toe Game (2-player mode)"""
    board = [[" "] * 3 for _ in range(3)]
    players = ['X', 'O']
    
    def display_board():
        for row in board:
            print(" | ".join(row))
            print("-" * 5)
    
    def check_winner():
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False
    
    print("\nWelcome to Tic-Tac-Toe!")
    display_board()
    
    for turn in range(9):
        player = players[turn % 2]
        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Invalid move. Try again.")
            continue
        display_board()
        if check_winner():
            print(f"Player {player} wins!")
            return
    print("It's a draw!")


def word_guess():
    """Word Guessing Game"""
    words = ["python", "game", "terminal", "interactive", "coding"]
    word = random.choice(words)
    print("\nGuess the word!")
    scrambled = ''.join(random.sample(word, len(word)))
    print("Scrambled word: ", scrambled)
    guess = input("Your guess: ")
    print("Correct!" if guess == word else f"Wrong! The word was {word}")


def number_guess():
    """Number Guessing Game"""
    num = random.randint(1, 100)
    print("\nGuess a number between 1 and 100")
    while True:
        guess = int(input("Enter your guess: "))
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print("Correct! You won!")
            break


def text_adventure():
    """Simple Text-Based Adventure Game"""
    print("\nWelcome to the Adventure Game!")
    choice = input("You see a cave. Enter? (yes/no): ").lower()
    if choice == "yes":
        print("You found a treasure chest!")
    else:
        print("You missed an adventure!")


def madlibs():
    """Madlibs Game"""
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj = input("Enter an adjective: ")
    print(f"Once upon a time, a {adj} {noun} loved to {verb} all day!")


def main():
    games = {
        "1": word_chain,
        "2": hangman,
        "3": tic_tac_toe,
        "4": word_guess,
        "5": number_guess,
        "6": text_adventure,
        "7": madlibs
    }
    while True:
        print("\nChoose a game:")
        for num, game in games.items():
            print(f"{num}. {game.__name__}")
        choice = input("Enter choice or 'q' to quit: ")
        if choice == 'q':
            break
        if choice in games:
            games[choice]()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()