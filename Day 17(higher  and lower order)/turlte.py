from turtle import Turtle, Screen

nepal = Turtle()
screen = Screen()


def forward_movement():
    nepal.forward(10)


def backward_movement():
    nepal.backward(10)


def turn_left():
    print(nepal.heading())
    new_heading = nepal.heading() + 10
    nepal.setheading(new_heading)


def turn_right():
    print(nepal.heading())
    new_heading = nepal.heading() - 10
    print(new_heading())
    nepal.setheading(new_heading)


def clear():
    nepal.clear()
    nepal.penup()
    nepal.home()
    nepal.pendown()


screen.listen()
screen.onkey(forward_movement, "f")
screen.onkey(backward_movement, "b")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")

screen.onkey(clear, "c")
screen.exitonclick()
