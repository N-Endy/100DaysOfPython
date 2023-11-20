from turtle import Turtle
# X_COR_RIGHT = 350
# X_COR_LEFT = -350
# Y_COR = 0
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        # self.segments = []
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, y_cor)
        
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
