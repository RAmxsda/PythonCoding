from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(
            "/Python 100 days challenge/Day 18(Snake Game)/data.txt"
        ) as highscore:
            self.high_score = int(highscore.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 220)
        self.write(
            f"Score: {self.l_score} High_Score:{self.high_score} ",
            align="center",
            font=("Calibri", 16, "normal"),
        )

    def reset(self):
        if self.l_score > self.high_score:
            self.high_score = self.l_score
            with open(
                "/Python 100 days challenge/Day 18(Snake Game)/data.txt", mode="w"
            ) as highscore:
                highscore.write(str(self.high_score))
        self.l_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
