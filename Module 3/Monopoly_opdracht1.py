# Dani van Enk, 11823526
# Monopoly_opdracht1.py plays 10000 games of monopoly with 1 player
# and looks at the difference if the initial money is different.

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
def simuleer_potje_Monopoly(startgeld_speler):

    # variables and lists
    money = startgeld_speler
    position = 0
    worpen = 0
    buyable_streets = 0
    total_possesions = 0
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
        result = worp_met_twee_dobbelstenen()
        position += result

        # go round the board
        if position > 39:
            position -= 40
            money += 200

        # check if the street you landed on is possesed
        if board_values[position] > 0:
            if posessions[position] == 0 and\
            board_values[position] <= money:
                money -= board_values[position]
                posessions[position] = 1
                total_possesions += 1
        worpen += 1

    return worpen

# simulating a lot of games
def simuleer_groot_aantal_potjes_Monopoly(startgeld_speler):

    # variables & lists
    Npotjes = 10000
    potjes = 0
    total = 0
    sub_total = 0
    tries = []

    # loop while the no. of games is less then the desired no. of games
    while potjes < Npotjes:
        tries.append(simuleer_potje_Monopoly(startgeld_speler))

        # print the average turns to posses the whole board, after 500 games
        if potjes % 500 == 0:
            for count in range(0, len(tries)):
                sub_total += tries[count]
            average = sub_total / float(len(tries))
            print "Initial money $" + str(startgeld_speler) + ",-"
            print "After " + str(potjes) + "/" + str(Npotjes),
            print "games, the average turns to posses",
            print "the whole board was %.4f" % average
            sub_total = 0
        potjes += 1

    # print the total average turns to posses the whole board after Npotjes games
    for count in range(0, len(tries)):
        total += tries[count]
    average = int(total / float(len(tries)))

    print " "
    print "Monopoly simulator: 1 player,",
    print "$" + str(startgeld_speler) + ",- initial money,",
    print str(Npotjes) + " games"
    print "After " + str(Npotjes),
    print "the average turns to posses the whole board was" + str(average)
    print " "
    return average

# execute simuleer_groot_aantal_potjes_Monopoly() with different initial money
money = 3000
start_geld = []
turns = []
while money >= 0:
    turns.append(simuleer_groot_aantal_potjes_Monopoly(money))
    start_geld.append(money)
    money -= 500

# plots the average turns it takes to fill the whole board
# with a certain inital money
pyplot.plot(start_geld, turns, 'b-')
pyplot.xlabel('starting money in $', fontsize=10)
pyplot.ylabel('# of turns', fontsize=10)
pyplot.xlim(0, 3000)
pyplot.show()

# readers note, histogram of the trump-mode was suspended because of exercise 2
