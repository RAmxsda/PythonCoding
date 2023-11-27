from turtle import Turtle

Distance_covered = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()

    def create_snake(self):
        for position in range(0, 4):
            self.add_segment(position)
            self.snake_segment[0].color("red")

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x=-20 * position, y=0)
        segment.speed("fastest")
        self.snake_segment.append(segment)

    def extend(self):
        self.add_segment(len(self.snake_segment[-1].position()))

    def snake_move(self):
        for segment in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[segment - 1].xcor()
            new_y = self.snake_segment[segment - 1].ycor()
            self.snake_segment[segment].goto(new_x, new_y)

        self.snake_segment[0].forward(Distance_covered)

    def up(self):
        if self.snake_segment[0].heading() != DOWN:
            self.snake_segment[0].setheading(UP)
            self.snake_move()

    def down(self):
        if self.snake_segment[0].heading() != UP:
            self.snake_segment[0].setheading(DOWN)
            self.snake_move()

    def left(self):
        if self.snake_segment[0].heading() != RIGHT:
            self.snake_segment[0].setheading(LEFT)
            self.snake_move()

    def right(self):
        if self.snake_segment[0].heading() != LEFT:
            self.snake_segment[0].setheading(RIGHT)
            self.snake_move()
