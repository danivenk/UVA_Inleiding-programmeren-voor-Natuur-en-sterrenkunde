# priemgetal.py vind de nde term in de priemreeks

# prime_checker() checkt of een cijfer een prime is
def prime_checker(ko):
    for i in range(2, ko):
        if ko % i == 0:
            return False
    return True

# variables
n = int(raw_input("Vind de nde term in de priemreeks: "))
m = 1
k = 1

# exclude alles kleiner of gelijk aan 0
while n <= 0:
    n = int(raw_input("Vind de nde term in de priemreeks: "))
# vind het nde priemgetal

while m <= n:
    k += 1
    if prime_checker(k):
        m += 1
print k