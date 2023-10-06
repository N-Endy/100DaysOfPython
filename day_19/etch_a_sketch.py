# w forward, s backwards, a left, d right, c clears drawing and turtle in center

# import turtle and screen for display
# create turtle
# listen for events
# function to make turtle move forward
# function ti make turtle move backwards
# function to make turtle move left
# function to make turtle move right
# if c is click screen clears with turtle in center

from turtle import Turtle, Screen

nel = Turtle()
nel.shape("turtle")
screen = Screen()


def move_up():
    nel.setheading(90)
    nel.forward(10)
    
def move_down():
    nel.setheading(270)
    nel.forward(10)

def move_right():
    nel.setheading(0)
    nel.forward(10)

def move_left():
    nel.setheading(180)
    nel.forward(10)
    
def clear_screen():
    nel.clear()
    nel.penup
    nel.home()
    nel.pendown()

screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()