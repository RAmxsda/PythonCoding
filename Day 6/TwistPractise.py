import random
import worldlist

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

list = ["HajurAama", "Baba", "Mummy", "Baini", "Hari"]

# Choose a random item from a list
choose = random.choice(list)
choose = choose.lower()
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

    # Checking if the guess is in the word
    for position in range(word_length):
        letter = choose[position]
        if letter == guess:
            guessed_letters[position] = letter
    if guess not in choose:
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
