import random
from ascii_art import STAGES
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def get_valid_letter():
    """Get a input that is o letter and only one character long"""
    while True:
        try:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Invalid input. Please enter a single alphabetical character.")

            return guess  # gültiger Buchstabe

        except ValueError as e:
            print(e)

def play_again():
    """Get an input whether the player wants to play again or not and return true or false"""
    while True:
        try:
            guess = input("Do you want to play again? (y/n): ").lower()

            if guess not in ["y","n"]:
                raise ValueError("Invalid input. Please enter y or n.")

            return guess == "y" # returns True if input is "y" and False if input is "n"

        except ValueError as e:
            print(e)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows the current state of the snowman and the correctly guessed letters"""

    print(STAGES[mistakes]) #displays snowman
    print()
    word_with_underscores = []
    for i in range(len(secret_word)):
        if secret_word[i] in guessed_letters:
            word_with_underscores.append(secret_word[i])
        else:
            word_with_underscores.append("_")

    word_with_underscores_text = " ".join(word_with_underscores)
    print(word_with_underscores_text)

    return word_with_underscores

def initialize_new_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    display_game_state(mistakes, secret_word, guessed_letters)  # initial game display
    return secret_word,mistakes,guessed_letters

def play_game():
    print("Welcome to Snowman Meltdown!")

    secret_word, mistakes, guessed_letters = initialize_new_game()
    # Gameloop
    running = True
    while running:
        guess = get_valid_letter()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        words_with_underscores = display_game_state(mistakes, secret_word, guessed_letters) #update game display

        #check if won or lost
        if "_" not in words_with_underscores:
            print(f"You guessed the word {secret_word} correctly!")
            if play_again():
                print("Let's play again!")
                secret_word, mistakes, guessed_letters = initialize_new_game()
            else:
                break
        # For now, simply prompt the user once:

        if mistakes == 5:
            print("Your snowman melted...")
            if play_again():
                print("Let's play again!")
                secret_word, mistakes, guessed_letters = initialize_new_game()
            else:
                running = False

    print("Goodbye :)")

