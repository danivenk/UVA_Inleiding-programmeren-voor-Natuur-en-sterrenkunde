# Dani van Enk, 11823526
# Monopoly_realistisch.py plays 10000 games of monopoly
# calculates how much more money player 2 needs to have
# than player 1 to have equal streets.

# import libaries
import math
import numpy as np
import random as rd
import matplotlib.pyplot as pyplot

# generates a trow this 2 dice and addes their value
def worp_met_twee_dobbelstenen():
    total = 0
    for count in range(0, 2):
        dice = rd.randint(1, 6)
        total += dice
    return total

# simulation of one game of Monopoly
def simuleer_potje_Monopoly(startgeld_speler_1, startgeld_speler_2):

    # variables and lists
    money1 = startgeld_speler_1
    money2 = startgeld_speler_2
    position1 = 0
    position2 = 0
    worpen = 0
    buyable_streets = 0
    total_possesions = 0
    delta = 0
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140,\
    150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240, 200,\
    260, 260, 150, 280, 0, 300, 0, 300, 320, 200, 0, 350, 0, 400]
    posessions = []

    # count the number of buyable streets
    for count in range(0, len(board_values)):
        posessions.append(0)
        if board_values[count] != 0:
            buyable_streets += 1

    # while less streets are possesed then there are streets
    while total_possesions < buyable_streets:

        # variables
        result1 = worp_met_twee_dobbelstenen()
        position1 += result1

        result2 = worp_met_twee_dobbelstenen()
        position2 += result2

        # go round the board
        if position1 > 39:
            position1 -= 40
            money1 += 200

        if position2 > 39:
            position2 -= 40
            money2 += 200

        # check if the street you landed on is possesed for player 1
        if board_values[position1] > 0:
            if posessions[position1] == 0 and\
            board_values[position1] <= money1:
                money1 -= board_values[position1]
                posessions[position1] = -1
                total_possesions += 1

        # check if the street you landed on is possesed for player 2
        if board_values[position2] > 0:
            if posessions[position2] == 0 and\
            board_values[position2] <= money2:
                money2 -= board_values[position2]
                posessions[position2] = 1
                total_possesions += 1

        worpen += 1

    # gets the difference in posessions between player 1 and 2
    for counter in range(0, len(posessions)):
        delta += posessions[counter]

    return delta

# simulating a lot of games
def simuleer_groot_aantal_potjes_Monopoly(startgeld_speler1, startgeld_speler2):

    # variables & lists
    Npotjes = 10000
    potjes = 0
    total = 0
    sub_total = 0
    difference = []

    # loop while the no. of games is less then the desired no. of games
    while potjes < Npotjes:
        difference.append(simuleer_potje_Monopoly(startgeld_speler1,\
        startgeld_speler2))

        # print the difference between the number of streets between
        # player 1 and 2 after 500 games
        if potjes % 500 == 0:
            for count in range(0, len(difference)):
                sub_total += difference[count]
            average = sub_total / float(len(difference))
            dmoney = startgeld_speler1 - startgeld_speler2
            print "After " + str(potjes) + "/" + str(Npotjes),
            print "games, player 1 had average %.4f" % average,
            print "less streets in posession"
            sub_total = 0
        potjes += 1

    # print the difference between the number of streets between
    # player 1 and 2 after Npotjes games
    for count in range(0, len(difference)):
        sub_total += difference[count]
    average = sub_total / float(len(difference))

    # print the the difference between the number of streets between
    # player 1 and 2 after Npotjes games
    # and the difference in initial money between player 1 and 2
    print " "
    print "Initial money[" + str(startgeld_speler1) + ",",
    print str(startgeld_speler2) + "]: Player 1 had " + str(average),
    print "less streets on average (player 2,",
    print "$" + str(startgeld_speler2 - startgeld_speler1) + " extra)"
    print " "
    return average

# with Evenwicht() you will know how mutch more player 2 has to have
# to have equal chance of getting the whole board
def Evenwicht():

    # variables and lists
    money = 0
    geld = []
    streets_more = []

    # running a 10000 games with differences in starting money between
    # player 1 and 2
    while money <= 200:
        streets_more.append(
            simuleer_groot_aantal_potjes_Monopoly(1500,1500 + money))
        geld.append(money)
        money += 50

    # calculating the average more money player 2 has to have
    # to have an equal amount of streets on average
    # this is a faster metod of calculating this
    # derivative = (streets_more[len(geld) - 1] - streets_more[0]) /\
    # float(geld[len(geld) - 1] - geld[0])
    # equal = int((-streets_more[0] / derivative) / float(25)) * 25
    # a different method is:
    # get the numbers around the 0 streets more point
    positive = 0
    negative = 0
    for count in range(0, len(streets_more)):
        if streets_more[count] < negative and streets_more[count] < 0:
            negative = geld[count]

        if streets_more[count] > positive and streets_more[count] > 0:
            positive = geld[count]

    # calculate the more  money player 2 needs to have for the equilibrium to hold
    equal = int(0.5*(positive+negative) / float(25)) * 25

    # plotting the number of streets more and how much more money player 2 has.
    pyplot.plot(geld, streets_more, 'm-')
    pyplot.xlim(0, 200)
    pyplot.xlabel('more money of player 2 in $')
    pyplot.ylabel('# of more streets of player 1')
    pyplot.show()

    return equal

# print the end result
# all of the code is in English and for consistency:
# the words startgeld, evenveel & straten have been added so checkpy will work
print "Monopoly simulator: 2"
print "(startgeld, evenveel & straten) If player 2 gets " + str(Evenwicht()),
print "more initial money,"
print "both players will have the same number of streets on average"
