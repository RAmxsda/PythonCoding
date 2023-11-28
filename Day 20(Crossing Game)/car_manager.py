from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(200, random.randint(-250, 250))
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def create_cars(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            self.add_car()

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE)

    def level_up(self):
        global MOVE
        MOVE += MOVE_INCREMENT
