# Dani van Enk, 11823526
#plot.py plot de grafiek x^x en vind het minimum.
import matplotlib.pyplot as pyplot
import math
import numpy as np

x_values = []
y_values = []
x_coord = []
y_coord = []
for x in np.arange(0, 1.5, 0.01):
    y = x**x
    x_values.append(x)
    y_values.append(y)

# In de volgende forloop wordt de minimale y waarde bepaald.
# Als de afgeleide van de functie 0 is, is er een minimum/maximum. In dit geval is de afgeleide van x^x, x^x*(ln(x)+1).
# Er worden 2 waardes vergeleken, y_value en y. Waarbij y_value de vorige y-waarde is.
# Als y_value kleiner dan 0 is en y groter dan 0.
# Betekend dit dat het punt rond y = 0 gevonden is en dus is het minimum gevonden als men die punten invult in de functie.
y_value = -4
for x in np.arange(0.01, 1.5, 0.01):
    y = x**x*(math.log(x) + 1)
    if y > 0 and y_value < 0:
        min_x = x
        x_coord.append(min_x)
        min_y = min_x**min_x
        y_coord.append(min_y)
        print "minimum: (", min_x, ", ", min_y, ")"
    y_value = y

pyplot.plot(x_values, y_values, 'b-')
pyplot.plot(x_coord, y_coord, 'ro')
pyplot.xlabel('x', fontsize=20)
pyplot.ylabel('y', fontsize=20)
pyplot.axis([0, 1.5, 0.6, 2])
# pyplot.text(4.00, 0.50, "$f(x)$ = $x^{x}$", color='black', fontsize=20)
pyplot.text(0.2, 0.8, r"(xmin,ymin) = ($0.37$, $0.69$)", color='black', fontsize=10)
pyplot.show() 
