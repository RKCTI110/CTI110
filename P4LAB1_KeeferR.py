# CTI 110
# P4LAB1 - Turtles
# KeeferR
# 11/12/24

# draw shapes and snowflakes using for loops

# Set up the turtle
import turtle
t = turtle.Turtle()
#background
win = turtle.Screen()
win.bgcolor("black")

# add some display options
t.pensize(6)
t.pencolor("white")
t.shape("turtle")

#Snowflake
for side in range(9):
    t.forward(100)
    t.lt(45)
    t.fd(50)
    t.rt(180)
    t.fd(50)
    t.lt(45)
    t.fd(50)
    t.rt(180)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(180)
    t.fd(150)
    t.rt(45)

t.pu()
t.fd(250)
t.pd()
#triangle
t.pensize(3)
t.pencolor("blue")
for side in range(3):
    t.forward(100)
    t.right(120)
t.pu()
t.fd(250)
t.pd()

#square
t.pencolor("cadetblue4")
for side in range (4):
    t.forward(100)
    t.left(90)
    


