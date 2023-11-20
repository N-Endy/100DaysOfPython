from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer()

r_paddle = Paddle()
l_paddle = Paddle()

# Move paddle
# screen.listen()
# screen.onkey(paddle.move_up, "Up")
# screen.onkey(paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()