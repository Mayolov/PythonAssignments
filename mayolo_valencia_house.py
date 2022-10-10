# Mayolo Valencia
#9/15/2021
# a "turtle" module is called upon giving it the name alex
# in a for loop the turtle first makes a sqaure then makes a
# triangle in a seperate for loop

# imports turtle module
import turtle

# sets turtle screen to (wn)
wn = turtle.Screen()

# sets the turtle to the name alex
alex = turtle.Turtle()

# for loop to make the square of the house loops 4 times
for i in range(4):
    alex.forward(150)
    alex.right(90)

# for loop to make the triangle and loops 3 times
for i in range(3):
    alex.forward(150)
    alex.left(120)

# user clicks on screen and it stops running
wn.exitonclick()