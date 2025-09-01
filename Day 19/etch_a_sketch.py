from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_back():
    tim.backward(20)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def reset_tim():
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(reset_tim, "c")

screen.exitonclick()