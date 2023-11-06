# Blackjack card games

import random

from click import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 11, 11, 11, 2]


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0 or user_score > 21:
        return "Robot Won"
    elif user_score > computer_score or computer_score > 21 or computer_score == 0:
        return "Human Won"


def playgame():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"{user_cards} , Human_Current score:{user_score}")
        print(f"{computer_cards},Robot_Current score:{computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want another card? Type 'y' or 'n': ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        if user_score > 21:
            is_game_over = True
            break
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Human_Final score:{user_score}")
    print(f"Robot_Final score:{computer_score}")
    print(compare_score(user_score, computer_score))


while input(f"enter 'y' if you want to play a game of blackjack \n") == "y":
    clear()
    playgame()
