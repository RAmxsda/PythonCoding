import random

print("Welcome to the Number Guessing room \n")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1, 100)
print(random_number)




def guess_numbers(attempts):
    while attempts > 0:
        guess_number = int(input("Make a guess \n"))
        if guess_number == random_number:
            print("You got it right")
            break

        elif guess_number > random_number and (guess_number - random_number) <= 10:
            print("you are little high")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")

        elif guess_number > random_number:
            print("Too high")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")

        elif guess_number < random_number and (random_number - guess_number) <= 10:
            print("you are little low")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")

        elif guess_number < random_number:
            print("Too low")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number")


if level == "easy":
    attempts = 6
    print(f"You have {attempts} remaining to guess the number")
    guess_numbers(attempts)


elif level == "hard":
    attempts = 4
    print(f"You have {attempts} remaining to guess the number")
    guess_numbers(attempts)
