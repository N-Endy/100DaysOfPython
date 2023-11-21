from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

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

# Initialize board
score_board = ScoreBoard()

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
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    
    # Ball bounce off wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        
    # Collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # R Paddles misses the ball
    if ball.xcor() > 380:
        score_board.increase_l_score()
        ball.reset_position()
        
    # R Paddles misses the ball
    if ball.xcor() < -380:
        score_board.increase_r_score()
        ball.reset_position()


screen.exitonclick()