from turtle import Screen
from paddle import Paddle
from ball import Ball

# Initialize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Initialize paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Initialize ball
ball = Ball()

# Move right paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Move left paddle
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Game condition
game_is_on = True
while game_is_on:
    screen.update()









screen.exitonclick()