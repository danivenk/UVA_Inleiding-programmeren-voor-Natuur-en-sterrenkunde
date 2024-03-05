# Dani van Enk, 11823526
# rieman.py calculates the intergral of 3 functions using the riemann-summation
# import libaries
import math
import numpy as np
import random as rd
import matplotlib.pyplot as pyplot

# function 1 x^(x+0.5)
def f1_of_x(x):
    return math.pow(x, (x + 0.5))

# function 2 tan(cos(sin(x)))
def f2_of_x(x):
    return math.tan(math.cos(math.sin(x)))

# function 3 sin(x^2)
def f3_of_x(x):
    return math.sin(x**2)

# riemann() gives the intergral output of a function using the Riemann-method
def riemann(f_of_x, a, b, n):
    # variables and lists
    block = a
    total = 0
    dn = (b-a)/float(n)
    # adds all areas of the small blocks along the interval [a,b] with n blocks
    while block < b:
        total += dn*(f_of_x(block+dn/float(2)))
        block += dn

    #printing and returning the total
    print "the total area is %.5f"%total
    return total

# executing the riemann() for functio 1 to 3
riemann(f1_of_x, 0, 1.0, 100000)
riemann(f2_of_x, 0.2, 2.2, 100000)
riemann(f3_of_x, 0, math.pi, 100000)