import random
from replit import clear

# HANGMAN PRACTICE
from wordlist import word_list
from worldlist_art import stages, logo


# Choose a random item from a list
choose = random.choice(word_list)
choose = choose.lower()

print(logo)
print(f"the choosen word is {choose}")

lives = 6

# Creating a empty list to store the letters
guessed_letters = []
word_length = len(choose)
for i in range(word_length):
    guessed_letters.append("_")
print(guessed_letters)

end_of_game = False
while not end_of_game:
    # Guessing a leeter
    guess = input("Guess a letter: ").lower()

    clear()

    # if user has already entered a letter they've already guessed, don't penalize them
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue

    # Checking if the guess is in the word
    for position in range(word_length):
        letter = choose[position]
        if letter == guess:
            guessed_letters[position] = letter
    if guess not in choose:
        print(f"You guessed {guess}, that's not in the word.
               You lose a life")
        lives -= 1
        print(lives)
        if lives == 0:
            end_of_game = True
            print("You loose")

    print(f"{' '.join(guessed_letters)}")
    if "_" not in guessed_letters:
        end_of_game = True
        print("You win")

    print(stages[lives])
