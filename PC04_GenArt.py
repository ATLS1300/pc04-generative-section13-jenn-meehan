"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Jenn Meehan

********* HEY, READ THIS FIRST **********

This is a variation on my pseudocode from PC03. The patterns change everytime due to the random feature but the 
layout stays the same. Thee inside pattern will almost always be more complicated than the outside pattern. I feel
this represents how, as people, we tend to be more complex on the inside. I chose purple,  orange, and black 
because Halloween is coming up and I'm very excited.

"""
import turtle
import math, random

turtle.colormode(255)
turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
panel.bgcolor("black") # sets background color

turtle.Turtle(visible=False) # create a turtle, make it invisible 
shape1 = turtle.Turtle() # sets up first turtle
shape2 = turtle.Turtle() # sets up second turtle
shape1.color(148,0,211) #sets color of first turtle

#===================
# YOUR CODE HERE!

# making the inner pattern
inShapeSize = 50
inShapeSides = random.randint(4,8) # changes the shape
inShapeAngle = 360/inShapeSides

inShapeInc = 10 # angle increment between shapes in pattern
inShapeIt = int(360/inShapeInc) # the number of iterations to make a complete circle. 
inShapeInner = 20 # radius of inner circle

shape1.up()
shape1.goto(0,100) # starting point for the turtle

# actually drawing the inner pattern
for inShapeIteration2 in range(inShapeIt):
    shape1.down()
    for inShapeIteration1 in range(inShapeSides):
        shape1.forward(inShapeSize)
        shape1.right(inShapeAngle)
    shape1.up()
    shape1.forward(inShapeInner)
    shape1.right(inShapeInc)

shape2.up()
shape2.color(255,127,80)
shape2.goto(-4,158) # this makes the outer pattern centered, more or less

outShapeSize = 50
outShapeSides = random.randint(3,5) # changes the shape
outShapeAngle = 360/outShapeSides

outShapeInc = 10 # angle increment between shapes in pattern
outShapeIt = int(360/outShapeInc) # the number of iterations to make a complete circle. 
outShapeInner = 30 # radius of outer circle

# drawing the outer pattern
for outShapeIteration2 in range(outShapeIt):
    shape2.down()
    for outShapeIteration1 in range(outShapeSides):
        shape2.forward(outShapeSize)
        shape2.right(outShapeAngle)
    shape2.up()
    shape2.forward(outShapeInner)
    shape2.right(outShapeInc)

panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
