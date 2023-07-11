from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.updatescoreBoard()

    def updatescoreBoard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="Center", font=("Courier", 50, "normal"))

        self.goto(100, 180)
        self.write(self.r_score, align="Center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.updatescoreBoard()

    def r_point(self):
        self.r_score += 1
        self.updatescoreBoard()