# Mayolo Valencia
# 10/7/2021
# making functions so the given program could run properly
# using many different ways of mean and reciprocal

# importing math module
import math

# this function gives the reciprocal of a given integer
# 8 -> .125  .125 -> 8
def reciprocal(x):
    reciprocated = 1 / x
    return reciprocated

# the three given values are placed when the function is called
# then adds them all together and divided to get the mean
def mean(a, b, c):
    average = (a + b + c) / 3
    return average

# 3 values are pulled from the called function, its multiplied then
# gets cube rooted
def geometric_mean(a, b, c):
    geo_tot = math.pow(a * b * c, reciprocal(3))
    return geo_tot

# gets 3 values, reciprocates them, adds them, and the they divide
# the amount of numbers in the denomenator
def harmonic_mean(a, b, c):
    har_mean = 3 / (reciprocal(a) + reciprocal(b) + reciprocal(c))
    return har_mean

def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")

    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.3.999...]")
  
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")

# runs the main function
main()