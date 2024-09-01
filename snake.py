from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.Segment = []
        self.create_snake()
        self.head = self.Segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("red")
        new_segment.goto(position)
        self.Segment.append(new_segment)

    def extend(self):
        self.add_segment(self.Segment[-1].position())

    def move(self):
        for seg_num in range(len(self.Segment) - 1, 0, -1):
            new_x = self.Segment[seg_num - 1].xcor()
            new_y = self.Segment[seg_num - 1].ycor()
            self.Segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
