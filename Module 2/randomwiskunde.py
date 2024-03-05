# Dani van Enk, 11823526
# randomwiskunde.py calculates the average number of random generations it takes to sum to 1
# and does this 1000000 times
# import libaries
import math
import numpy as np
import random as rd

# gives the average number of random number generation to 1 after 1000000
def randomwiskunde():
    tries = 0
    total = 0
    counting = []

    # looping the summation till 1, 1000000 times
    while tries < 1000000: 
        number = 0
        counter = 0
        
        # generating random numbers up to 1
        while number < 1:
            number += rd.random()
            counter += 1
        counting.append(counter)
        tries += 1
    
    for count in range(0, len(counting)-1):
        total += counting[count]
    average = total/float(len(counting))
    print "Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is: %.4f" %average

randomwiskunde()