# Dani van Enk, 11823526
# afstand.py determines the average distance in a square of 1 by 1
# import libaries
import math
import numpy as np
import random as rd

# the average distance function
def vierkant():
    # veriables and list
    tries = 0
    total = 0
    distance = 0
    distance_vierkant = []

    # calculation of 1000000 times the distance between 2 points
    while tries < 1000000:
        x1 = rd.random()
        x2 = rd.random()
        y1 = rd.random()
        y2 = rd.random()
        distance = math.sqrt(float((x2-x1)**2 + (y2-y1)**2))
        distance_vierkant.append(distance)
        tries += 1
    
    # get the average of all distances calculated in the while before
    for count in range(0, len(distance_vierkant)-1):
        total += distance_vierkant[count]
    average = total/float(len(distance_vierkant))
    return average

# printing out the average
print "the average distance in a square of 1.00 x 1.00 is: ", vierkant()