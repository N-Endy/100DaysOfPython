from turtle import Turtle, Screen
nel = Turtle()
screen = Screen()


def move_forward():
    nel.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()