# Dani van Enk, 11823526
# histogram.py makes a histogram of the average of 100 random numbers between 0 and 100 and loops this 10000 times
# it also displays the percentage of average above the 60 and below the 40
# import libaries
import math
import numpy as np
import random as rd
import matplotlib.pyplot as pyplot

# SomeRandomGetallen() gives a list of 10000 times the average of 100 random numbers between 0 and 100
def SomRandomGetallen():
    tries = 0
    random_numbers = []

    # looping 10000 times
    while tries < 10000:
        counter = 0
        random_number = 0

        # adding 100 random numbers between the 0 and the 100
        while counter < 100:
            random_number += 100*rd.random()
            counter += 1
        average = float(random_number / 100)
        random_numbers.append(average)
        tries += 1
    return random_numbers

# lists
rn = SomRandomGetallen()
number40 = []
number60 = []

# checking if there are averages that are less then 40 or more then 60
for counting in range(0, len(rn)-1):
    random = rn[counting]
    if random <= 40:
        number40.append(random)
    elif random >= 60:
        number60.append(random)

# calculating the percentage of less then 40 and more then 60
percentage40 = len(number40)/float(len(rn))*100
percentage60 = len(number60)/float(len(rn))*100

# print the percentages
print "%.2f%% (below average 40)" %percentage40
print "%.2f%% (above average 60)" %percentage60

# plot de histogram
pyplot.xlim(30,70)
pyplot.hist(rn, bins=50)
pyplot.show()
