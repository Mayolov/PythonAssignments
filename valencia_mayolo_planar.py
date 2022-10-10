# Mayolo Valencia
# 10/7/2021
# user inputs the x and y coordinates individually
# when the variables finally have a value they go down
# to the print statement and get placed into the function
# in the distance() function it uses the math.pow to sqaure
# root the problem after all the values are asigned in the parameters
# the second print function gives the block distance and gets the absolute
# value of the variables from the parameters and ads both sides together

#import math module
import math

# gets the linear distance between points and returns the value
def distance(x1, y1, x2, y2):
    line_dist = math.pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 1/2)
    return line_dist

# gets the block distance between 2 points and returs the calue
def block_distance(x1, y1, x2, y2):
    block = abs(x1 - x2) + abs(y1 - y2)
    return block

# asks the user to input points then prints after the functions
# are called
def main():
    # asks user to input both points to run
    x1 = float(input('input x coord for first point: '))
    y1 = float(input('input y coord for first point: '))
    x2 = float(input('input x coord for second point: '))
    y2 = float(input('input y coord for second point: '))
    
    # puts the users inputs into the function parameters and
    # prints the distance
    print('Pythagorean distance: ', \
          format(distance(x1, y1, x2, y2),'.2f'))
    print('City block distance: ', \
          format(block_distance(x1, y1, x2, y2),'.2f'))
    
# call main to run everything
main()
