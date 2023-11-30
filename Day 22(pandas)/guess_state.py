from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("US states Guessing Game")
image = "/Python 100 days challenge/Day 22(pandas)/blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()

turtle.shape(image)

data = pandas.read_csv("/Python 100 days challenge/Day 22(pandas)/50_states.csv")
all_states = data.state.to_list()


guessed_states = []

while len(guessed_states) < 50:
    state = screen.textinput(
        title=f"Guess the state {len(guessed_states)}/50  states ",
        prompt="What's another state name?",
    ).title()

    if state == "Exit":
        missing_states = [
            states for states in all_states if states not in guessed_states
        ]
        # missing_states = []
        # for states in all_states:
        #     if states not in guessed_states:
        #         missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("/Python 100 days challenge/Day 22(pandas)/states_to_learn.csv")
        break

    # if the guessing of user is correct
    if state in all_states:
        guessed_states.append(state)
        print("Correct")
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state) or
        t.write(state_data.state.item())  # to get the state name from the csv file

screen.exitonclick()
