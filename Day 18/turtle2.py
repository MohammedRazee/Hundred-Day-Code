from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.fd(5)
    tim.up()
    tim.fd(5)
    tim.down()

screen = Screen()
screen.exitonclick()