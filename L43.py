# the authors names are Gwyneth and Victoria
import turtle
romeo = turtle.Turtle()
juilet = turtle.Turtle()

juilet.color("misty rose")
juilet.width(3)

romeo.color("violet")
romeo.width(3)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range (185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if romeo_last_name == "montague" : #It's just one little change down here.
    juilet.left(140)
    juilet.forward(100)
    for side in range(185):
        juilet.forward(1)
        juilet.right(1)
    juilet.hideturtle()
