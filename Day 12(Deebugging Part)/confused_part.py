from click import clear
from art import logo, vs
from data import data
import random


def Comparing_followers(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return "person1"
    elif person1["follower_count"] == person2["follower_count"]:
        return "Both have the same amount of followers"
    else:
        return "person2"


def play_game():
    score = 0
    person1 = random.choice(data)
    person2 = random.choice(data)
    game_continue = True
    while game_continue:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")

        person1 = person2
        person2 = random.choice(data)

        while person1 == person2:
            person2 = random.choice(data)

        print(
            f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}"
        )
        print(vs)
        print(
            f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}"
        )

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        result = Comparing_followers(person1, person2)

        clear()
        if (user_choice == "a" and result == "person1") or (
            user_choice == "b" and result == "person2"
        ):
            print("You're right! sore:{score}")
            score += 1
        else:
            game_continue = False

            print(f"Sorry, that's wrong. Your final score: {score}")
            break


play_game()
