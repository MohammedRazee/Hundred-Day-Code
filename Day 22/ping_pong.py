from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating the scoreboard
scoreboard = Scoreboard()

# Creating the Paddles from a class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball
ball = Ball()

# User controls with setup
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# Game running
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()