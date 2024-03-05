# Dani van Enk, 11823526
# spiraal.py makes a plot of a spiral with the polar curve R = 10 - 0.5*alpha
# import libaries
import math
import numpy as np
import matplotlib.pyplot as pyplot

# converting a polar curve into cartesian points
for alpha in np.arange(0, 20, 0.1):
    R = 10 - 0.5 * alpha
    x = R * math.cos(alpha)
    y = R * math.sin(alpha)

    # plotting the spiral
    pyplot.plot(x, y, 'bo')
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    pyplot.xlabel('x', fontsize=10)
    pyplot.ylabel('y', fontsize=10)
    pyplot.draw()
    pyplot.pause(0.01)
