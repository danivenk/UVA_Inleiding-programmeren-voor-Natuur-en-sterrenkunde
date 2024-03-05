# Dani van Enk, 11823526
# reeks.py vind de langste reeks van niet priemgetallen onder de 10000 (extentie naar variable max included)

# variables and lists
# when using a variable n use n = int(raw_input("geeft een getal: "))
number = 10000
prime = []
non_prime = [1]
dummy = []

# main loop
for some_number in range(2, number+1):
    devided = 0
    for another_number in range(2, some_number):
        if some_number % another_number == 0:
            devided += 1
            break
    if devided == 0:
        prime.append(some_number)
        if len(dummy) <= len(non_prime):
            dummy = []
            dummy = non_prime
            non_prime = []
        else:
            non_prime = []
    else:
        non_prime.append(some_number)

print "De langste reeks niet-priemgetallen onder de", number, "begint op", dummy[0], "en eindigt bij", dummy[len(dummy) - 1]
print "De reeks is", len(dummy), "lang."
