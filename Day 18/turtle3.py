from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "CadetBlue1"]

def draw_shape(num):
    angle = 360 / num
    for _ in range(num):
        tim.fd(100)
        tim.right(angle)

for n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(n)
    

screen = Screen()
screen.exitonclick()
