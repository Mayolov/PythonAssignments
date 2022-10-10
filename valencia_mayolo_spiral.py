# Mayolo Valencia
# 9/15/2021
# This program asks users to input sides of a polygon,
# how many spins itll do, and a percent increase in arm
# length. It all gets calculated to later be put into a for loop.
# It imports a turtle module and runs the user inputs on a screen
# to show a spiraling polygon

# imports turtle module
import turtle

#initializing base arm length
arm_length = 10

# user inputs how many sides the polygon has
sides = int(input("How many sides for this plygon:? "))

# how many iterations the for loop is going to loop
spins = int(input("How many spins? "))

# asks for how much user wants each arm to grow more per iteration
arm_increase = float(input("Prefered percent increase of arms ? "))

# calculates the degrees for the calculates sides
degrees_angle = 360 / sides

# calculates the perecent increase for the arms of the spiral
arm_multiple = arm_increase / 100

# sets a variable to the turtle screen
wn = turtle.Screen()

# turtle 1 and pensize increase
alex = turtle.Turtle()
alex.pensize(1.1)

# object 1a
for i in range(spins):
    # goes forward 10 plus user set iterations at a user
    # set multiplier and goes right at the calculated degrees
    arm_length += arm_length * arm_multiple
    alex.forward(arm_length)
    alex.right(degrees_angle)

# when turtles finish the user can click
# anywhere and shut the screen off
wn.exitonclick()