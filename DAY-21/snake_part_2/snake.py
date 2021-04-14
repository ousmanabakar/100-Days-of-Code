from turtle import Turtle
POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head_of_the_snake = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[snake_num - 1].xcor()
            new_y_cor = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x_cor, new_y_cor)
        self.head_of_the_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_of_the_snake.heading() != DOWN:
            self.head_of_the_snake.setheading(UP)

    def down(self):
        if self.head_of_the_snake.heading() != UP:
            self.head_of_the_snake.setheading(DOWN)

    def left(self):
        if self.head_of_the_snake.heading() != RIGHT:
            self.head_of_the_snake.setheading(LEFT)

    def right(self):
        if self.head_of_the_snake.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
