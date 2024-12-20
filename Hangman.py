'''Implement your solution in this file.
Make sure that you decompose your solution into appropriate 
functions and that you include appropriate documentation.'''

import random
import string

def load_words(filename):
    """Load a list of words from a file."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)

def is_valid_guess(guess):
    """Check if the guess is a valid single letter."""
    return len(guess) == 1 and guess.isalpha()

def hangman():
    words = load_words("words.txt")
    secret_word = choose_word(words)
    guessed_word = ['-' for _ in secret_word]
    letters_guessed = set()
    warnings = 3
    guesses = 10

    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings and 10 guesses to start.")

    while guesses > 0 and '-' in guessed_word:
        print("-" * 20)
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {''.join(sorted(set(string.ascii_lowercase) - letters_guessed))}")
        print(f"Current word: {''.join(guessed_word)}")

        guess = input("Please guess a letter: ").lower()

        if not is_valid_guess(guess):
            if warnings > 0:
                warnings -= 1
                print(f"Invalid input. You have {warnings} warnings left.")
            else:
                guesses -= 1
                print("Invalid input. You lost a guess.")
            continue

        if guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(f"You already guessed that letter. You have {warnings} warnings left.")
            else:
                guesses -= 1
                print("You already guessed that letter. You lost a guess.")
            continue

        letters_guessed.add(guess)

        if guess in secret_word:
            print("Good guess!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            if guess in vowels:
                guesses -= 2
                print(f"{guess} is not in the word. You lost 2 guesses.")
            else:
                guesses -= 1
                print(f"{guess} is not in the word. You lost 1 guess.")

    print("-" * 20)

    if '-' not in guessed_word:
        unique_letters = len(set(secret_word))
        score = guesses * unique_letters
        print(f"Congratulations, you won! Your score is {score}.")
    else:
        print(f"You ran out of guesses. The word was {secret_word}.")

if __name__ == "__main__":
    hangman()
