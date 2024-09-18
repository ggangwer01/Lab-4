# the authors names are Gwyneth and Victoria
import turtle
jack = turtle.Turtle()
jack.color("yellow")
for side in range (4):
    jack.forward(100)
    jack.right(90)

import turtle
john = turtle.Turtle()
john.color("yellow")
for side in range (4):
    if side == 3:
        john.color("magenta")
john.forward(100)
john.right(90)
