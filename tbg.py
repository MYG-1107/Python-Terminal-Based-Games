import random
import time

def tic_tac_toe():
    """Tic-Tac-Toe game against AI"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    ai = "O"
    
    def print_board():
        for row in board:
            print(" | ".join(row))
            print("-" * 5)
    
    def check_winner():
        for row in board:
            if row.count(row[0]) == 3 and row[0] != " ":
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return True
        return False
    
    def ai_move():
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        if empty_cells:
            return random.choice(empty_cells)
        return None
    
    turn = 0
    while True:
        print_board()
        if turn % 2 == 0:
            print("Player X, enter your move (row and column, e.g., 0 1): ")
            try:
                row, col = map(int, input().split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = player
                else:
                    print("Invalid move! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Enter two numbers between 0 and 2.")
                continue
        else:
            print("AI is making a move...")
            time.sleep(1)
            move = ai_move()
            if move:
                board[move[0]][move[1]] = ai
        
        if check_winner():
            print_board()
            print(f"{'Player' if turn % 2 == 0 else 'AI'} wins!")
            break
        turn += 1
        if turn == 9:
            print("It's a draw!")
            break

def number_guessing():
    """Number guessing game where the player guesses a number between 1 and 100"""
    number = random.randint(1, 100)
    attempts = 0
    
    print("Guess a number between 1 and 100!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Enter a number.")

def word_chain():
    """Word Chain Game where players take turns saying words that start with the last letter of the previous word"""
    words_used = []
    
    print("Welcome to the Word Chain game!")
    word = input("Start with a word: ").strip().lower()
    words_used.append(word)
    
    while True:
        last_letter = word[-1]
        next_word = input(f"Enter a word starting with '{last_letter}': ").strip().lower()
        if next_word in words_used:
            print("Word already used! You lose.")
            break
        elif not next_word or next_word[0] != last_letter:
            print("Invalid word! It must start with the last letter of the previous word.")
        else:
            words_used.append(next_word)
            word = next_word

def hangman():
    """Classic Hangman game where the player guesses letters to find the word"""
    words = ["python", "developer", "terminal", "challenge", "code"]
    word = random.choice(words)
    guessed = ["_" for _ in word]
    attempts = 6
    
    print("Welcome to Hangman!")
    while attempts > 0:
        print("Word: ", " ".join(guessed))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        
    if "_" in guessed:
        print(f"Game over! The word was {word}.")

def main():
    """Main function to select and play games"""
    games = {
        "1": ("Tic-Tac-Toe (AI)", tic_tac_toe),
        "2": ("Number Guessing", number_guessing),
        "3": ("Word Chain", word_chain),
        "4": ("Hangman", hangman),
    }
    
    while True:
        print("\nChoose a game:")
        for key, (name, _) in games.items():
            print(f"{key}. {name}")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Thanks for playing! Goodbye!")
            break
        elif choice in games:
            games[choice][1]()
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()