# Rock Paper scissor game

import random

rock = '🪨';
paper ='📝';
scissor= '✂️';

game_images = [rock, paper, scissor]

print("Welcome to Rock Paper Scissor Game\n")
user = int(input("What's your choice? '0' for rock, '1' for paper, '2' for scissors\n"));
print("You choose: ", game_images[int(user)])
computer = random.randint(0,2)
print("Computer choose: ", game_images[int(computer)])

if user >=3 or user < 0:
    print("You typed an invalid number, you lose!")

elif user == computer:
    print("It's a tie!")

# elif user == 0 and computer == 2:
#     print("You loose!")

elif user > computer:
    print("You win!")

elif user < computer:
    print("You loose!")

