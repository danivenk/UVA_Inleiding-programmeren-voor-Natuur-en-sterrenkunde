# Dani van Enk, 11823526
# -*- coding: utf-8 -*-
# temperatuur.py analyses the data from DeBiltTempMax.txt and DeBiltTempMin.txt

# import
import matplotlib.pyplot as pyplot

# Month() will convert the MM part of a YYYYMMDD date into
# it's respective monthname
def Month(month):
    months = ["January", "February", "March", "April", "May", "June",\
    "July", "August", "September", "October", "November", "December"]

    returnmonth = " " + str(months[month]) + " "
    return returnmonth

# ConvertToYears() converts the date YYYYMMDD to years
def ConvertToYears(date):

    # check if leapyear
    if int(date[:4]) % 4 == 0:
        daysinyear = 366
    else:
        daysinyear = 365

    # sum the total date in years
    totdate = int(date[:4]) + int(date[4:-2]) / float(12) +\
    int(date[6:]) / float(daysinyear)

    # return it
    return totdate

# TempMax() will find the highest temperature in the dataset DeBiltTempMax.txt
# and it's corresponding date
def TempMax():

    # input file
    input_filehandle = open('DeBiltTempMax.txt', 'r')

    # list & variables
    data = []
    maximumtemp = []
    date = []
    lineno = 0
    tempmax = 0

    # puts all data from the input file into a list 
    for line in input_filehandle:
 
        # exclusion of the explanation stops at line 17
        if lineno > 17:

            # with separation mark ',' for the rows
            separated_data = line.split(',')
            data.append(separated_data)
        lineno += 1

    # finds certain titles in the first list of the data list
    for counter in range(0, len(data[0])):

        # searches for TX (temperature)
        if data[0][counter] == "   TX":

            # puts all temperature data points in a list
            for count in range(1, len(data)):
                temp = int(data[count][counter])
                maximumtemp.append(temp/10)

                # finds the maximum temperature
                if temp > tempmax:
                    tempmax = temp

                    # finds the maximum temperature date
                    # converts it to a readable date format
                    if data[0][counter - 1] == "    DATE":
                        time = int(data[count][counter - 1][4:-2]) - 1
                        word = str(data[count][counter - 1][:4]) + \
                            Month(time) + str(data[count][counter - 1][6:])

        # searches for DATE
        if data[0][counter] == "    DATE":

            # puts all dates (in years) into a list
            for count in range(1, len(data)):
                cdate = ConvertToYears(data[count][counter])
                date.append(cdate)

    # converts maximum temperature to degrees
    maximum = tempmax / float(10)

    # prints the maximum temperature with corresponding date
    print "The hottest day in the Bilt was on " + word + " with " +\
    str(maximum) + " degrees Celsius"

    #returning the maximumtemp list and datelist for the temperature plot
    return maximumtemp, date

    # close the file
    input_filehandle.close()

# TempMin() will find the lowest temperature in the dataset DeBiltTempMin.txt
# and it's corresponding date
def TempMin():

    # input file
    input_filehandle = open('DeBiltTempMin.txt', 'r')

    # lists and variables
    data = []
    minimumtemp = []
    date = []
    lineno = 0
    tempmin = 0

    # puts all data from the input file into a list
    for line in input_filehandle:

        # exclusion of the explanation stops at line 17
        if lineno > 17:

            # with separation mark ',' for the rows
            separated_data = line.split(',')
            data.append(separated_data)
        lineno += 1

    # finds certain titles in the first list of the data list
    for counter in range(0, len(data[0])):

        # searches for TN (temperature)
        if data[0][counter] == "   TN":

            # puts all temperature data points in a list
            for count in range(1, len(data)):
                temp = int(data[count][counter])
                minimumtemp.append(temp / 10)

                # finds the lowest temperature
                if temp < tempmin:
                    tempmin = temp

                    # finds the minimum temperature date
                    # converts it to a readable date format
                    if data[0][counter - 1] == "    DATE":
                        time = int(data[count][counter - 1][4:-2]) - 1
                        word = str(data[count][counter - 1][:4]) + \
                            Month(time) + str(data[count][counter - 1][6:])

        # searches for DATE
        if data[0][counter] == "    DATE":

            # puts all dates (in years) into a list
            for count in range(1, len(data)):
                cdate = ConvertToYears(data[count][counter])
                date.append(cdate)

    # converts minimum temperature to degrees
    minimum = tempmin / float(10)

    # prints the minimum temperature with corresponding date
    print "The coldest day in the Bilt was on " + word + " with " +\
    str(minimum) + " degrees Celsius"

    #returning the minimumtemp list and datelist for the temperature plot
    return minimumtemp, date

    # close the file
    input_filehandle.close()

# freeze() find the longest period of frost (maximum < 0degrees Celsius)
# between 1901 and 2016
def freeze():

    # input file
    input_filehandle = open('DeBiltTempMax.txt', 'r')

    # lists and variable
    data = []
    dummytemp = []
    dummydate = []
    tempminus = []
    dateminus = []
    lineno = 0

    # puts all data from the input file into a list
    for line in input_filehandle:

        # exclusion of the explanation stops at line 17
        if lineno > 17:

            # with separation mark ',' for the rows
            separated_data = line.split(',')
            data.append(separated_data)
        lineno += 1

    # finds certain titles in the first list of the data list
    for counter in range(0, len(data[0])):

        # searches for TX (temperature)
        if data[0][counter] == "   TX":

            # finds the longest freezing period (> 0degrees Celsius)
            for count in range(1, len(data)):

                # check if temperature was below 0
                if int(data[count][counter]) < 0:
                    tempminus.append(data[count][counter])
                    dateminus.append(data[count][counter - 1])

                else:

                    # keep the longest frostperiod list
                    if len(dummytemp) < len(tempminus):
                        dummytemp = tempminus
                        tempminus = []
                        dummydate = dateminus
                        dateminus = []

                    else:
                        tempminus = []
                        dateminus = []

    # length and time variables
    length = len(dummydate) - 1
    time = int(dummydate[length][4:-2]) - 1

    # print the longest period of frost in the Bilt
    print "The coldest period in the Bilt was " + str(length + 1) +\
    " days long and ended on " + dummydate[length][:4] +\
    Month(time) + dummydate[length][6:]

# Tropisch() finds tropical days (< 30degrees Celsius) and summer days (< 25degrees Celsius) in the Bilt
def Tropisch():

    # input file
    input_filehandle = open('DeBiltTempMax.txt', 'r')

    # lists and variable
    data = []
    summerday = [0]
    tropicday = [0]
    years = []
    lineno = 0
    summer = 0
    tropic = 0

    # puts all data from the input file into a list
    for line in input_filehandle:

        # exclusion of the explanation stops at line 17
        if lineno > 17:

            # with separation mark ',' for the rows
            separated_data = line.split(',')
            data.append(separated_data)
        lineno += 1

    # finds certain titles in the first list of the data list
    for counter in range(0, len(data[0])):

        # searches for TX (temperature)
        if data[0][counter] == "   TX":

            # puts tropical and summer days in a list
            for count in range(1, len(data)):
                temp = int(data[count][counter])
                year = int(data[count][counter - 1][:4])
                date = int(data[count][counter - 1][4:])

                # check if summerday or tropical day
                if temp > 250:
                    summer += 1
                if temp > 300:
                    tropic += 1
                
                # if new year comes put all the summer and tropic days in lists
                if date == 101:
                    summerday.append(summer)
                    tropicday.append(tropic)

                    summer = 0
                    tropic = 0

    # create a list with all years between 1900 and 2015
    for counting in range(1900, 2016):
        years.append(counting)

    # returning the summerday and tropicalday lists for histogram
    return summerday, tropicday, years

def heatwave():

    # input file
    input_filehandle = open('DeBiltTempMax.txt', 'r')

    # lists and variable
    data = []
    summerday = []
    tropicday = []
    countable = []
    lineno = 0
    heat = 0
    tropicheat = 0

    # puts all data from the input file into a list
    for line in input_filehandle:

        # exclusion of the explanation stops at line 17
        if lineno > 17:

            # with separation mark ',' for the rows
            separated_data = line.split(',')
            data.append(separated_data)
        lineno += 1

    # finds certain titles in the first list of the data list
    for counter in range(0, len(data[0])):

        # searches for TX (temperature)
        if data[0][counter] == "   TX":

            # puts tropical and summer days in a list
            for count in range(1, len(data)):
                temp = int(data[count][counter ])
                date = int(data[count][counter - 1])

                # check if summerday or tropical day
                if temp > 250:
                    summerday.append(date)
                if temp > 300:
                    tropicday.append(date)

                else:

                    # check if the number of summerdays and
                    # tropicdays corresponds to a heatwave
                    if 5 <= len(summerday) and 3 <= len(tropicday):
                        print "The first heatwave was in the year "\
                        + str(date)[:4]
                        break

                    # if not reset the tropic and summer list
                    else:

                        summerday = []
                        tropicday = []

# temperature() plots all the data in figures
def temperature():
    # getting the data from TempMax(), TempMin() and Tropisch()
    maximumtemp, maxdate = TempMax()
    minimumtemp, mindate = TempMin()
    summerday, tropicday, year = Tropisch()

    # lists
    date = [1900,2016]
    zero = [0,0]

    # temperature also executes freeze()
    freeze()
    heatwave()

    # creates the x axis
    for count in range(0, len(maxdate)):
        date.append(maxdate[count])
        zero.append(0)

    # figure 1 plots the maximum and minimum temperatures
    pyplot.figure(1)
    pyplot.plot(maxdate, maximumtemp, 'r-', mindate, minimumtemp, 'b-',\
    date, zero, 'k-')
    pyplot.xlim(1900, 2016)
    pyplot.ylim(-40, 50)
    pyplot.xlabel("date in years")
    pyplot.ylabel("temperature in degrees Celsius")

    # figure 2 plots the tropical and summer days per year
    pyplot.figure(2)
    pyplot.plot(year, summerday, 'b-', year, tropicday, 'r-')
    pyplot.xlim(1900, 2015)
    pyplot.ylim(0, 65)
    pyplot.xlabel("date in years")
    pyplot.ylabel("number of tropical/summer days")
    pyplot.text(1900, 67, "red: tropicaldays\n blue: summerdays",\
    color="black", fontsize=10,)
    pyplot.show()

# execute temperature()
temperature()
