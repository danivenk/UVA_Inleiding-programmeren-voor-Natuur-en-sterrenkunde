# Dani van Enk, 11823526
# nulpunten.py vind de nulpunten van f(x)=ax^2+bx+c
# import libaries
import matplotlib.pyplot as pyplot
import math
import numpy as np

def nulpunten(a, b, c): 
    nul = []
    Discriminant = b**2-4*a*c
    if Discriminant >= 0:
        null = (-b + math.sqrt(Discriminant))/(float(2 * a))
        nul.append(null)
        null = (-b-math.sqrt(Discriminant))/(float(2*a))
        nul.append(null)
    return nul

a = 3#int(raw_input("What is a? "))
b = 7#int(raw_input("What is b? "))
c = -10#int(raw_input("What is c? "))
x_values = []
y_values = []
x_max = (-b)/(float(2*a))
x_axis = []
zero = []
crosspoints = nulpunten(a, b, c)
x1 = []
x2 = []

for x in np.arange(x_max-(10/float(a)), x_max+(10/float(a)), 0.01):
    x_values.append(x)
    y = a*math.pow(x, 2) + b*x + c
    y_values.append(y)
    x_axis.append(x)
    zero.append(0)

if 0 < len(crosspoints) <= 2:
    print crosspoints
elif len(crosspoints) == 0:
    print "Couldn't find any crossing points with the x-axis"

if b >= 0:
    plus_minus1 = "+"
else:
    plus_minus1 = "-"
    b = abs(b)
if c >= 0:
    plus_minus2 = "+"
else:
    plus_minus2 = "-"
    c = abs(c)

pyplot.plot(x_values, y_values, 'b-')
pyplot.plot(x_axis, zero, 'm--')
pyplot.plot(crosspoints, [0,0], 'ro')
pyplot.axis([x_max-(10/float(a)), x_max+(10/float(a)), -10*a, 10*a])
pyplot.text(x_max, 10*a, "$f(x) = $" + str(a) + "$x^{2}$" + plus_minus1 + str(b) + "$x$" + plus_minus2 + str(c),
    color='black', fontsize=20)
pyplot.text(crosspoints[0], 0, "$x_{1} =$" + str(crosspoints[0]), color='black', fontsize=10)
pyplot.text(crosspoints[1], 0, "$x_{2} =$" + str(crosspoints[1]), color='black', fontsize=10)
pyplot.show()
