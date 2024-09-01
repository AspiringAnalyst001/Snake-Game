from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("yellow")
        self.refresh()

    def refresh(self):
        margin_x = random.randint(-270, 270)
        margin_y = random.randint(-270, 270)
        self.goto(margin_x, margin_y)
