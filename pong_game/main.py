from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Move right paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Move left paddle
screen.listen()
screen.onkey(l_paddle.move_up, "Q")
screen.onkey(l_paddle.move_down, "A")

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()