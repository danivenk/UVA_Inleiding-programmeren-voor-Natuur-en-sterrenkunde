import math
import numpy as np
import matplotlib.pyplot as plt

speed = 1/float(1000)
# neem kleine stappen in x tussen 0 en 2pi
for x in np.arange(0,1, 0.01):

    y = math.sin(x*2*math.pi)

    # plot grafiek
    plt.plot(x, y, 'bo', markersize = 10)  # blauwe punt
    plt.xlim(0,1)
    plt.ylim(-1, 1)
    plt.draw()           # update grafiek
    plt.pause(speed)
    plt.clf()            # clear grafiek