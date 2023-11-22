import turtle as t
import random

nepal = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def make_spirograph(shift_gap):
    for data in range(int(360 / shift_gap)):
        nepal.speed("fastest")
        nepal.color(random_color())
        nepal.circle(80)
        nepal.setheading(nepal.heading() + shift_gap)


make_spirograph(3)
screen = t.Screen()
screen.exitonclick()
