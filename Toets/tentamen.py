# Dani van Enk, 11823526
# Note: all given functions, outputs and variables are Dutch
# the rest is English

# import
import math
import random as rd
import matplotlib.pyplot as pyplot

# This function gives the difference to the average of a list 
def Opgave1(L):

    # variables and list
    total = 0
    more_than_average = 0
    less_than_average = 0
    differencelist = []

    # summing all items in the list
    for counter1 in range(0, len(L)):
        total += L[counter1]

    # calculating the average
    average = total / float(len(L))

    # listing the difference between each item in the list and the average
    for counter2 in range(0, len(L)):

        # making the difference list
        difference = L[counter2] - average
        differencelist.append(difference)

        # checking if the difference is more or less then 0
        if difference > 0:
            more_than_average += 1
        elif difference < 0:
            less_than_average += 1
    
    # printing the result
    print "Het gemiddelde van de lijst getallen is " + str(average)
    print "Er zijn " + str(less_than_average) +\
    " waarden onder het gemiddelde en " + str(more_than_average) + " erboven"
    print "Afwijkingslijst = " + str(differencelist)
    print " "

# this exercise will calculate the area of an intergral using the montecarlo-method
def Opgave2():

    # lists & variable
    x_values = []
    y_values = []
    zero = []
    ypointg = []
    xpointg = []
    ypointr = []
    xpointr = []
    points = 0
    totalpoints = 100000

    # finding all y points and creating the x and 0 lists
    for x in range(1, 160):
        x_values.append(x/10.)
        zero.append(0)
        y = math.sin(x/10.) / (x/10.)
        y_values.append(y)

    # creating totalpoints points
    while points < totalpoints:

        # creating a random x and y coordinate
        randomx = math.pi * rd.random() + math.pi
        randomy = 1.4 * rd.random() - 0.4

        # checking if the randomy is bigger then the function and smaller then 0
        for counter in range(0, len(zero)):
            if randomy >= y_values[counter] and randomy <= 0:
                ypointg.append(randomy)
                xpointg.append(randomx)
                break
        
        # a point has been added
        points += 1

    # calculating the area
    part_of_graph = len(ypointg) / float(totalpoints)
    area = part_of_graph * 1.4 * math.pi

    # printing the result
    print "De oppervlakte = %.3f"% area
    print " "

    # plotting the graph
    pyplot.figure(0)
    pyplot.plot(x_values, y_values, 'b-', x_values, zero, 'k-', xpointg, ypointg, 'go')
    pyplot.xlim(0, 16)
    pyplot.ylim(-.4, 1)
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.show()

    # Sidenote: I could not get the area right, hope I was close enough

# this exercise checks what method calculates pi the best Leibniz or Euler
def Opgave3():

    # number of trieslist
    N = [10, 100, 1000, 10000]

    # excecuting the N list
    for counter in range(0, len(N)):

        # start Leibniz and Euler
        Leibniz = 0
        Euler = 0

        # Summing Leibniz
        for n in range(0, N[counter] + 1):
            Leibniz += math.pow(-1, n) / float(2 * n + 1)

        # Summing Euler
        for n in range(1, N[counter] + 1):
            Euler += 1 / float(n**2)
        
        # final calculations
        Leibniz *= 4
        Euler *= 6
        Euler = math.sqrt(Euler)

        # calculating the difference between the Euler/Leibniz pi and the real pi
        deltaLeib = math.sqrt((Leibniz / float(math.pi) * 100 - 100) ** 2)
        deltaEul = math.sqrt((Euler / float(math.pi) * 100 - 100) ** 2)

        # printing the first part
        print "n = " + str(N[counter]) + ": Leibniz = %.5f (delta = %.5f procent)"\
        % (Leibniz, deltaLeib)
        print "n = " + str(N[counter]) + ": Euler = %.5f (delta = %.5f procent)"\
        % (Euler, deltaEul)

        # printing who wins (who is the closest to pi)
        if deltaLeib < deltaEul:
            print "n = " + str(N[counter]) + ": Leibniz wint"
        else:
            print "n = " + str(N[counter]) + ": Euler wint"

        print " "

def Opgave4():

    # list
    abundantNumbers = []

    # looping for each number between 1 and 100
    for counter1 in range(1, 101):

        # devider list and variable
        deviders = [0]
        deviderstot = 0

        # getting 2 numbers between 1 and the current number (counter1)
        for counter2 in range(1, counter1):
            for counter3 in range(1, counter1):

                # checking of those numbers times each other are the current number
                if counter2 * counter3 == counter1:

                    # checking if thos numbers are already in the deviders list
                    for counter4 in range(0, len(deviders)):

                        # checking for number 1
                        if counter2 != deviders[counter4]:
                            deviders.append(counter2)

                        # checking for number 2
                        elif counter3 != deviders[counter4]:
                            deviders.append(counter3)
        
        # summing the deviders
        for counter5 in range(0, len(deviders)):

            # excluding the dubble deviders
            if deviders[counter5] != deviders[counter5 - 1]:
                deviderstot += deviders[counter5]

        # checking if the current number is an abundant number
        if deviderstot > counter1:
            abundantNumbers.append(counter1)

    # printing the result
    print "De lijst van abundante getallen onder de 100: "\
    + str(abundantNumbers)
    print " "

# this exercise will calculate the angle between two vectors in degrees
def Opgave5(V1, V2):

    # calculating the inproduct and the length of the 2 vectors
    V1_in_V2 = V1[0] * V2[0] + V1[1] * V2[1]
    Length_V1 = math.sqrt((V1[0]) ** 2 + (V1[1]) ** 2)
    Length_V2 = math.sqrt((V2[0]) ** 2 + (V2[1]) ** 2)

    # calculating the angle and converting it to degrees
    theta_rad = math.acos(V1_in_V2 / float(Length_V1 * Length_V2))
    theta_deg = theta_rad * (180 / float(math.pi))

    # printing the result
    print "De hoek tussen de vectoren (%i,%i) en (%i,%i) is "\
    % (V1[0], V1[1], V2[0], V2[1]) + str(theta_deg) + " graden"

# given lists
L = [2,3,7,6,0,12,3,7,9,6]
V1 = [1,2]
V2 = [3,4]

# execute the exercises
Opgave1(L)
Opgave2()
Opgave3()
Opgave4()
Opgave5(V1, V2)
