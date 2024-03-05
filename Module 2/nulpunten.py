# Dani van Enk, 11823526
# nulpunten.py finds the roots of the function f(x)=ax^2+bx+c
# import libaries
import matplotlib.pyplot as pyplot
import math
import numpy as np

# function for finding cosspoints with the x-axis
def nulpunten(a, b, c): 
    nul = []
    Discriminant = b**2-4*a*c

    if Discriminant >= 0:
        null = (-b + math.sqrt(Discriminant))/(float(2 * a))
        nul.append(null)
        null = (-b-math.sqrt(Discriminant))/(float(2*a))
        nul.append(null)
    return nul

# variables
a = 1
b = 2
c = -10
x_max = (-b)/(float(2*a))
crosspoints = nulpunten(a, b, c)

# lists
x_values = []
y_values = []
x_axis = []
zero = []
x1 = []
x2 = []

#for loop for creating the function f(x)=ax^2+bx+c and y=0
for x in np.arange(x_max-(10/float(a)), x_max+(10/float(a)), 0.01):
    x_values.append(x)
    y = a*math.pow(x, 2) + b*x + c
    y_values.append(y)
    x_axis.append(x)
    zero.append(0)

# check if there are any crosspoints
if 0 < len(crosspoints) <= 2:
    print crosspoints
elif len(crosspoints) == 0:
    print "Couldn't find any crossing points with the x-axis"

# create the correct +/- signs for in the function text
if b >= 0:
    plus_minus1 = "+"
else:
    plus_minus1 = "-"
    b = -b
if c >= 0:
    plus_minus2 = "+"
else:
    plus_minus2 = "-"
    c = -c

# creating the plot of f(x)=ax^2+bx+c, the x-axis and their crossing points
pyplot.plot(x_values, y_values, 'b-')
pyplot.plot(x_axis, zero, 'm--')
pyplot.plot(crosspoints, [0,0], 'ro')
pyplot.axis([x_max-(5/float(a)), x_max+(5/float(a)), -20*a, 20*a])
pyplot.text(x_max, 20*a, "$f(x) = $" + str(a) + "$x^{2}$" + plus_minus1 + str(b) + "$x$" + plus_minus2 + str(c),
            color='black', fontsize=20)
pyplot.text(crosspoints[0], 0-2*a,"$x_{1} = %.2f$" %crosspoints[0], color='black', fontsize=10)
pyplot.text(crosspoints[1], 0-2*a,"$x_{2} = %.2f$" %crosspoints[1], color='black', fontsize=10)
pyplot.show()
