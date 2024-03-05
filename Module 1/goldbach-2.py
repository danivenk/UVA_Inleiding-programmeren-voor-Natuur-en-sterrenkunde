# goldbach.py maakt gebruik van de stelling van Goldbach

# prime_checker() checkt of een cijfer een prime is
def prime_checker(ko):
    for i in range(2, ko):
        if ko % i == 0:
            return False
    return True

# variables and lists
n = int(raw_input("geef een cijfer: "))
prime = []
even = []
# main loop
for i in range(2, n + 1):
    if prime_checker(i):
        prime.append(i)
for k in range(4, n+1):
    if k % 2 == 0:
        even.append(k)
for l in range(0, len(even)):
    print even[l], "=",
    p = True
    r = False
    for m in range(0, len(prime)):
        for o in range(0, len(prime)):
            if prime[m] + prime[o] == even[l]:
                if prime[m] <= prime[o] and p:
                    print prime[m], "+", prime[o]
                    p = False
    if r == False:
        print even[l], "Bingo"
