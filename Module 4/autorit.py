# Dani van Enk, 11823526
# autorit.py analyses the data from a car journey AutoRitData.csv

# import libararies
import math
import matplotlib.pyplot as pyplot

# input file
input_filehandle = open('AutoRitData.csv', 'r')

# lists
data = []
time = []
speed = []
latitude = []
longitude = []
latitudeg = []
latituder = []
longitudeg = []
longituder = []
dspeed = []
dtime = []

# variables
distance = 0
speedmax = 0

# create a data list from the opened file
# first separated_data list wil contain all table titles (like: time, speed etc.)
for line in input_filehandle:
    separated_data = line.split(',')
    data.append(separated_data)

# create lists from the datalist
for counter in range(0, len(data[0])):

    # create a list of time and delta time
    if data[0][counter] == "locTimeStamp":
        for count in range(1, len(data)):
            current_time = int(data[count][counter]) - 1416383865
            deltatime = 1

            dtime.append(deltatime)
            time.append(current_time)

    # create a list of the latitude
    elif data[0][counter] == "lat":
        for count in range(1, len(data)):
            latitude.append(float(data[count][counter]))

    # create a list of the longitude
    elif data[0][counter] == "long":
        for count in range(1, len(data)):
            longitude.append(float(data[count][counter]))

    # create a list of the speed
    elif data[0][counter] == "speed":
        for count in range(1, len(data)):
            current_speed = float(data[count][counter]) * 3.6

            # test for maxspeed (for the axis)
            if speedmax < current_speed:
                speedmax = current_speed

            # checks if the speed exceeds 50km/h ( > 50km/h red, < 50km/h green)
            if current_speed < 50:
                latituder.append(latitude[count - 1])
                longituder.append(longitude[count - 1])
            elif current_speed > 50:
                latitudeg.append(latitude[count - 1])
                longitudeg.append(longitude[count - 1])

            # appending the speed to lists
            speed.append(current_speed)
            dspeed.append(current_speed/float(3.6))

# determinating the total distance
for counting in range(0, len(dspeed)):
    dt = dtime[counting]
    dv = math.sqrt(dspeed[counting]**2)

    distance += dv * dt

# printing total distance in km
print "the total distance is %.2f km"% (distance / float(1000))

# plot 1 is a time,speed plot
pyplot.figure(1)
pyplot.plot(time, speed, 'b-')
pyplot.xlim(0, current_time)
pyplot.ylim(0, speedmax)
pyplot.xlabel("time in s", fontsize=10)
pyplot.ylabel("speed in km/h", fontsize=10)

# plot 2 is a map (long,lat) with the +/- 50km/h points
pyplot.figure(2)
pyplot.plot(longituder, latituder, 'ro', longitudeg, latitudeg, 'go')
pyplot.xlabel("longitude in degrees", fontsize=10)
pyplot.ylabel("latitude in degrees", fontsize=10)
pyplot.show()

# close the file
input_filehandle.close()
