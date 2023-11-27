# Cookies
# Author:
# 21 November 2023

import turtle

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")
def make_cookie(x: int, y: int):
    """draws a cookie on the screen at (x,y)
    
    params:
    x - is the x coordinate of the center of the cookie
    y - is the y coordinate at the center of the cookie
    """
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.circle(30)
    baker_turtle.penup()
    
    baker_turtle.color("black")
    #center
    baker_turtle.goto(0+x, 0+y)
    baker_turtle.stamp()

    baker_turtle.goto(10+x,10+y)
    baker_turtle.stamp()

    baker_turtle.goto(-10+x,-10+y)
    baker_turtle.stamp()

    baker_turtle.goto(10+x,-10+y)
    baker_turtle.stamp()

    baker_turtle.goto(-10+x,10+y)
    baker_turtle.stamp()

make_cookie(100,100)
make_cookie(0,0)
make_cookie(50,50)
turtle.done()