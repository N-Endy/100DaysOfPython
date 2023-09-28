from turtle import Turtle, Screen
import tkinter as TK
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.width(5)
color = ["navy", "cyan", "dark goldenrod", "magenta", "maroon", "indigo"]
degree = [0, 90, 180, 270]

# for i in color:
#     timmy.color(i)
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(2000):
#     timmy.color(random.choice(color))
#     timmy.forward(5)
#     timmy.up()
#     timmy.forward(5)
#     timmy.down()

# for side in range(3, 11):
#     timmy.color(random.choice(color))
#     for _ in range(side):
#         timmy.forward(100)
#         timmy.right(360/side)


for _ in range(200):
    timmy.color(random.choice(color))
    timmy.forward(10)
    timmy.right(random.choice(degree))





screen = Screen()
screen.exitonclick()