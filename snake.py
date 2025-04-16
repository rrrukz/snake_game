from turtle import Turtle

START_POSITION=((0,0),(-20,0),(-40,0))


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)


    def right(self):
        self.segments[0].setheading(360)

    def left(self):
        self.segments[0].setheading(180)
