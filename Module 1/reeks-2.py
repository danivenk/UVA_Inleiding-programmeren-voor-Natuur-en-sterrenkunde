# reeks.py vind de langste reeks van niet priemgetallen onder de 10000 (extentie naar variable max included)

# prime_checker() checkt of een cijfer een prime is
def prime_checker(ko):
    for i in range(2, ko):
        if ko % i == 0:
            return False
    return True

# variables and listss
n = 10000 #int(raw_input("geeft een getal: "))
prime = []
non_prime = [1]
dummy = []

# main loop
for i in range(2, n+1):
    if prime_checker(i):
        prime.append(i)
        if len(dummy) <= len(non_prime):
            dummy = []
            dummy = non_prime
            non_prime = []
        else:
            non_prime = []
    else:
        non_prime.append(i)
print "De langste reeks niet-priemgetallen onder de",
print n,
print "begint op",
print dummy[0],
print "en eindigt bij",
print dummy[len(dummy)-1]
print "De reeks is",
print len(dummy),
print "lang."
