# Dani van Enk, 11823526
# montecarlo.py calculates the intergrals of 4 functions using the Monte-Carlo method
# import libaries
import math
import numpy as np
import random as rd
import matplotlib.pyplot as pyplot

# function 1 x^(x+0.5)
def f1_of_x(x):
    return math.pow(x, (x+0.5))

# function 2 tan(cos(sin(x)))
def f2_of_x(x):
    return math.tan(math.cos(math.sin(x)))

# function 3 sin(x^2)
def f3_of_x(x):
    return math.sin(x**2)

# montecarlo() calculates the area (intergrall)
def montecarlo(f_of_x, x1, y1, x2, y2):
    # variables and lists
    tries = 0
    x_values = []
    y_values = []
    x_pointxt = []
    y_pointyt = []
    x_pointxtmin = []
    y_pointytmin = []
    x_pointxf = []
    y_pointyf = []

    # creates the graph of the input function f_of_x
    for x in np.arange(x1, x2, 0.01):
        x_values.append(x)
        y_values.append(f_of_x(x))

    # draws all random points in the [x1,x2] and [y1, y2] intervals
    while tries < 20000:
        pointx = (x2-x1)*rd.random()+x1
        pointy = (y2-y1)*rd.random()+y1

        # puts the points into the correct lists, x_pointxf/y_pointyf voor buiten de funtie
        # x_pointxt/y_pointyt voor tussen de grafiek en y = 0 voor de grafiek boven de x-as
        # x_pointxtmin/y_pointytmin voor tussen de grafiek en y = 0 voor de grafiek onder de x-as
        if f_of_x(pointx) >= 0 and pointy > f_of_x(pointx):
            x_pointxf.append(pointx)
            y_pointyf.append(pointy)
        elif f_of_x(pointx) >= 0 and pointy < 0:
            x_pointxf.append(pointx)
            y_pointyf.append(pointy)
        elif f_of_x(pointx) >= 0 and pointy <= f_of_x(pointx):
            x_pointxt.append(pointx)
            y_pointyt.append(pointy)
        elif f_of_x(pointx) <= 0 and pointy < f_of_x(pointx):
            x_pointxf.append(pointx)
            y_pointyf.append(pointy)
        elif f_of_x(pointx) <= 0 and pointy > 0:
            x_pointxf.append(pointx)
            y_pointyf.append(pointy)
        elif f_of_x(pointx) <= 0 and pointy >= f_of_x(pointx):
            x_pointxtmin.append(pointx)
            y_pointytmin.append(pointy)
        tries += 1

    # prints the total area
    area = (x2-x1)*(y2-y1)
    good = (len(y_pointyt)-len(y_pointytmin))/float(len(y_pointyt)+len(y_pointyf)+len(y_pointytmin))
    tot_area = good*area
    print "the total area is %.5f"% tot_area

    # plots de grafieken en de random punten
    pyplot.plot(x_values, y_values, 'b-')
    pyplot.plot(x_pointxt, y_pointyt, 'go')
    pyplot.plot(x_pointxtmin, y_pointytmin, 'yo')
    pyplot.plot(x_pointxf, y_pointyf, 'ro')
    pyplot.xlabel('x', fontsize=20)
    pyplot.ylabel('y', fontsize=20)
    pyplot.axis([x1, x2, y1, y2])
    pyplot.show()

    # returns the total area
    return tot_area

# twitter_ei function creates the Twitter Egg and plots it with the average area every 100 tries
def TwitterEi():
    # variables and lists
    tries = 0
    hundred = 100
    area = 2 * 1.5
    tot = 25000
    pointinx = []
    pointiny = []
    pointoutx = []
    pointouty = []
    approx = []
    approy = []

    # gets tot random points and puts them in their respective lists
    while tries < tot:
        # while-loop variables which get reset every loop
        x = 2*rd.random()-1
        y = 1.5*rd.random()-0.5
        #creates lists with the points outside the function and inside the function
        if math.sqrt(x**2 + y**2) + 2/float(3)*math.sqrt(x**2 + (5/float(6) - y)**2) <= 1:
            pointinx.append(x)
            pointiny.append(y)
        elif math.sqrt(x**2 + y**2) + 2/float(3)*math.sqrt(x**2 + (5/float(6) - y)**2) >= 1:
            pointoutx.append(x)
            pointouty.append(y)

        # get the approximate area every 100 tries
        if tries == hundred-1:
            good = (len(pointiny))/float(len(pointiny) + len(pointouty))
            tot_area = good*area
            approy.append(tot_area)
            good = (len(pointiny)) / float(len(pointiny) + len(pointouty))
            tot_area = good * area
            approx.append(tries)
            hundred += 100
        tries += 1

    # gets the total area after tot tries and prints it
    good = (len(pointiny)) / float(len(pointiny) + len(pointouty))
    tot_area = good * area
    print "the total area of a Twitter Egg is %.5f"% tot_area

    # plots the Twitter Egg and the points outside it in blue
    pyplot.plot(pointoutx, pointouty, 'bo')
    pyplot.xlabel('x', fontsize=20)
    pyplot.ylabel('y', fontsize=20)
    pyplot.axis([-1, 1, -0.5, 1])
    pyplot.show()

    # plots the approximate area as a function of the number of tries every 100 tries
    pyplot.plot(approx, approy, 'r-')
    pyplot.xlabel('area', fontsize=10)
    pyplot.ylabel('tries', fontsize=10)
    pyplot.show()

    # returns the total area after tot tries
    return tot_area

# executes montecarlo() for the functions 1 to 3
montecarlo(f1_of_x, 0, 0, 1.0, math.pow(1, (1+.5)))
montecarlo(f2_of_x, 0.2, 0, 2.2, math.tan(math.cos(math.sin(0.2))))
montecarlo(f3_of_x, 0, -1, math.pi, 1)

# executes TwitterEi()
TwitterEi()
