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



