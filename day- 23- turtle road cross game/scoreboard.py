from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
