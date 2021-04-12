from turtle import Turtle

POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snakes_list = []
        self.create_snake()

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
        self.snakes_list[0].forward(MOVE_DISTANCE)
