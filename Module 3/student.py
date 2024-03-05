# Dani van Enk, 11823526
# student.py follows the path of 2 drunken Students
# import libaries
import math
import numpy as np
import random as rd
import matplotlib.pyplot as pyplot

# drunkenStudent() creates 2 drunken students and shows their paths for 200 steps
def drunkenStudent():
    # variables
    xg = 0
    yg = 0
    xr = 0
    yr = 0
    steps = 0
    maximum = 1

    # lists
    x_valuesg = []
    y_valuesg = []
    x_valuesr = []
    y_valuesr = []
    difference_step = [0]
    step = [0]

    # for-loop for doing the 200 steps
    for counter in range(0, 200):
        # lists & variables
        x_difference = []
        y_difference = []
        dxg = 2 * rd.random() - 1
        dyg = 2 * rd.random() - 1
        dxr = 2 * rd.random() - 1
        dyr = 2 * rd.random() - 1

        # addition to coordinates
        xg += dxg / float(2)
        yg += dyg / float(2)
        xr += dxr / float(2)
        yr += dyr / float(2)

        # out of range loops
        # these will adjust the paths of the students if they're out of range
        # using squaring and squarerooting to avoid infinite loops.
        # student 1, green
        while xg < -10:
            print "Out of range! Adjusting path"
            xg += math.sqrt((dxg / float(2))**2)
        while xg > 10:
            print "Out of range! Adjusting path"
            xg -= math.sqrt((dxg / float(2))**2)
        while yg < -10:
            print "Out of range! Adjusting path"
            yg += math.sqrt((dyg / float(2))**2)
        while yg > 10:
            print "Out of range! Adjusting path"
            yg -= math.sqrt((dxg / float(2))**2)

        # student 2, red
        while xr < -10:
            print "Out of range! Adjusting path"
            xr += math.sqrt((dxr / float(2))**2)
        while xr > 10:
            print "Out of range! Adjusting path"
            xr -= math.sqrt((dxr / float(2))**2)
        while yr < -10:
            print "Out of range! Adjusting path"
            yr += math.sqrt((dyr / float(2))**2)
        while yr > 10:
            print "Out of range! Adjusting path"
            yr -= math.sqrt((dyr / float(2))**2)

        # addition to lists of the coordinations
        # of the students and the differences
        x_difference.append(xg)
        x_difference.append(xr)
        y_difference.append(yg)
        y_difference.append(yr)

        x_valuesg.append(xg)
        y_valuesg.append(yg)
        x_valuesr.append(xr)
        y_valuesr.append(yr)

        # calculating the average distance between the 2 students
        difference = math.sqrt((x_difference[0] - x_difference[1])**2 + (
            y_difference[0] - y_difference[1])**2)
        difference_step.append(difference)
        steps += 1
        step.append(steps)

        # check the max difference for the y-axis maximum
        if difference > maximum:
            maximum = difference + 1

        # plotting the path of the students, the students and their differences
        pyplot.figure(1)
        pyplot.plot(x_valuesg, y_valuesg, 'g-', x_valuesr, y_valuesr, 'r-',\
        x_difference, y_difference, 'b-', xg, yg, 'go', xr, yr, 'ro')
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        pyplot.xlabel('x', fontsize=10)
        pyplot.ylabel('y', fontsize=10)
        pyplot.text(-8, -8, "%d/200 steps" % (counter))
        pyplot.draw()
        pyplot.pause(0.01)
        pyplot.clf()

        # plotting the average distance between the 2 students
        pyplot.figure(2)
        pyplot.xlim(0, counter)
        pyplot.ylim(0, maximum)
        pyplot.xlabel('# of steps', fontsize=10)
        pyplot.ylabel('distance between 2 students', fontsize=10)
        pyplot.plot(step, difference_step, 'm-')

# execute the drunkenStudent() function
drunkenStudent()
