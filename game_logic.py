import random
from ascii_art import STAGES
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

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


def play_game():
    secret_word = get_random_word()
    secret_word = "snowman"
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = []
    # Gameloop
    running = True
    while running:
        words_with_underscores = display_game_state(mistakes,secret_word,guessed_letters)

        if "_" not in words_with_underscores:
            print(f"You guessed the word {secret_word} correctly!")
            break
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        if mistakes == 3:
            print("Your snowman melted...")
            running = False



