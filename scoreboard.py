from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update()

    def gameover(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", True, ALIGNMENT, FONT)

    def update(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Your score = {self.score}", True, ALIGNMENT, FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
