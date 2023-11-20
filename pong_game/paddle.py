from turtle import Turtle
# X_COR_RIGHT = 350
# X_COR_LEFT = -350
# Y_COR = 0
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, x_cor, y_cor):
        # self.segments = []
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        pad = Turtle("square")
        pad.color("white")
        pad.shapesize(5, 1)
        pad.penup()
        pad.goto(x_cor, y_cor)
        
    def move_up(self):
        self.setheading(UP)

    def move_down(self):
        self.setheading(UP)
