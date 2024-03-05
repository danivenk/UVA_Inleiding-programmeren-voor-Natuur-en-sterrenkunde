# import
import matplotlib.pyplot as pyplot
import math
import numpy as np

x = []
y = []
G = -6.67*10**-11
M = 2.0*10**30

for i in np.arange(0, 2*math.pi, 0.01):
    x.append(math.cos(i))
    y.append(math.sin(i))

for k in range(0, len(y)):
    v = 

pyplot.figure(1)
pyplot.plot(x, y, 'r-')
pyplot.xlim(-2.0, 2.0)
pyplot.ylim(-1.5, 1.5)
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.show()