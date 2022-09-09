
from random import random
import turtle
test = turtle.Turtle()

test.speed(0)
""""
test.shape("arrow")

test.pensize(5)
test.shapesize(1)
test.forward(400)

test.forward(100)
test.back(50)
test.goto(-350,350)
test.sety(-150)

test.pencolor("random")
test.forward(100)"
"""
while True:
    test.right(2941)
    test.forward(2483)
    if abs(test.xcor()) > 400 or abs(test.ycor()) > 600:
        test.goto(0,0)


turtle.done()