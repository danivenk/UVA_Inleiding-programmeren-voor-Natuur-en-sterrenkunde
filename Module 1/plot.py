# Dani van Enk, 11823526
# plot.py plot de grafiek x^x en vind het minimum.
# import libaries
import matplotlib.pyplot as pyplot
import math
import numpy as np

y_min = 10000
x_values = []
y_values = []
x_coord = []
y_coord = []
# coordinaten loop voor de grafiek
for x in np.arange(0, 1.5, 0.01):
    y = x**x
    x_values.append(x)
    y_values.append(y)

# minimum loop
for x in np.arange(0, 1.5, 0.01):
    y = x**x
    if y_min <= y:
        min_x = x - 0.01
        x_coord.append(min_x)
        min_y = y_min
        y_coord.append(min_y)
        print "minimum: (", min_x, ", ", min_y, ")"
        break
    y_min = y

pyplot.plot(x_values, y_values, 'b-')
pyplot.plot(x_coord, y_coord, 'ro')
pyplot.xlabel('x', fontsize=20)
pyplot.ylabel('y', fontsize=20)
pyplot.axis([0, 1.5, 0.6, 2])
# pyplot.text(4.00, 0.50, "$f(x)$ = $x^{x}$", color='black', fontsize=20)
pyplot.text(0.2, 0.8, r"(xmin,ymin) = ($0.37$, $0.69$)",
            color='black', fontsize=10)
pyplot.show()
