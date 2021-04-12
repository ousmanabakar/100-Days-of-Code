from turtle import Turtle

POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.head_of_the_snake = self.snakes_list[0]

    def create_snake(self):
        for position in POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snakes_list.append(snake)

    def move(self):
        for snake_num in range(len(self.snakes_list) - 1, 0, -1):
            new_x_cor = self.snakes_list[snake_num - 1].xcor()
            new_y_cor = self.snakes_list[snake_num - 1].ycor()
            self.snakes_list[snake_num].goto(new_x_cor, new_y_cor)
        self.head_of_the_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_of_the_snake.heading() != DOWN:
            self.head_of_the_snake.setheading(UP)

    def down(self):
        if self.head_of_the_snake.heading() != UP:
            self.head_of_the_snake.setheading(DOWN)

    def left(self):
        if self.head_of_the_snake.heading() != DOWN:
            self.head_of_the_snake.setheading(LEFT)

    def right(self):
        if self.head_of_the_snake.heading() != LEFT:
            self.snakes_list[0].setheading(RIGHT)
