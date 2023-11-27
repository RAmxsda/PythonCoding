from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 220)
        self.write(
            f"Score: {self.l_score}", align="center", font=("Calibri", 16, "normal")
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Calibri", 16, "normal"))
        self.goto(0, -20)
        self.write(
            f"Score: {self.l_score}", align="center", font=("Calibri", 16, "normal")
        )

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
