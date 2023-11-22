import turtle as turtle_modal
import colorgram
import random

# rgb = []

# for color in colorgram.extract("image.jpg", 4):
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

# print(rgb)

rgb = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
]

turtle_modal.colormode(255)
nepal = turtle_modal.Turtle()
nepal.speed("fastest")
nepal.penup()
nepal.setheading(225)
nepal.forward(250)
nepal.setheading(0)
number_of_dots = 100

for _ in range(1, number_of_dots + 1):
    nepal.dot(20, random.choice(rgb))
    nepal.forward(40)
    if _ % 10 == 0:
        nepal.setheading(90)
        nepal.forward(40)
        nepal.setheading(180)
        nepal.forward(400)
        nepal.setheading(0)


screen = turtle_modal.Screen()
screen.exitonclick()
