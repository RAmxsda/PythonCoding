from turtle import Turtle, Screen
import random

is_race_on = False
nepal = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
all_nepals_turtle = []

for i in range(0, 6):
    nepal = Turtle(shape="turtle")
    nepal.color(colors[i])
    nepal.penup()
    nepal.goto(x=-230, y=y_coordinates[i])
    all_nepals_turtle.append(nepal)


if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_nepals_turtle:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
screen.exitonclick()
