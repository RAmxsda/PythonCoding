from turtle import Screen
from snake_class import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("green")
screen.title("Python Game")
screen.tracer(0)

snake = Snake()

food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.2)
    snake.snake_move()
    screen.update()

    # Detect collision with food
    if snake.snake_segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.l_point()

    # Detect collision with wall
    if (
        snake.snake_segment[0].xcor() > 245
        or snake.snake_segment[0].xcor() < -245
        or snake.snake_segment[0].ycor() > 245
        or snake.snake_segment[0].ycor() < -245
    ):
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snake_segment[1:]:
        if snake.snake_segment[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
