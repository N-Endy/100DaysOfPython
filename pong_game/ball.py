from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super.__init__()
        self.create_ball()
        
        
    def create_ball(self):
        self.shape("sphere")
        self.color("white")
        self.penup
        self.goto(0, 0)