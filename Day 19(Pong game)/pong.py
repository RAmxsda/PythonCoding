from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((-330, 0))
l_paddle = Paddle((330, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(l_paddle) < 50
        and ball.xcor() > 300
        or ball.distance(r_paddle) < 50
        and ball.xcor() < -300
    ):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 350:
        ball.rest_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -350:
        ball.rest_position()
        score.r_point()


screen.exitonclick()
