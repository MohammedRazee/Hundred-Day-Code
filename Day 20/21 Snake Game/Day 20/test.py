from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.fd(20)
tim.left(180)
tim.fd(30)

print(tim.heading())

screen.exitonclick()