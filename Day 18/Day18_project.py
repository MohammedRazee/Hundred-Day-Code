import turtle as t
import random

color_list = [(202, 164, 110), (149, 75, 50), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

def dotted_pattern():
    tim.speed("fastest")
    tim.penup()

    for n in range(-200, 300, 50):  
        tim.setposition(-200, n)
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
    tim.hideturtle()

dotted_pattern()

screen.exitonclick()
