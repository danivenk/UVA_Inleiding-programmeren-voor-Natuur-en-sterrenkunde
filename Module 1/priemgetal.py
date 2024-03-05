# Dani van Enk, 11823526
# priemgetal.py vind de nde term in de priemreeks

# variables
nth_prime = int(raw_input("Vind de nde term in de priemreeks: "))
mth_prime = 1
number = 1

# exclude alles kleiner of gelijk aan 0
while nth_prime <= 0:
    nth_prime = int(raw_input("Vind de nde term in de priemreeks: "))
# vind het nde priemgetal

while mth_prime <= nth_prime:
    number += 1
    divided = 0
    is_it = 0
    for some_number in range(2, number):
        if number % some_number == 0:
            divided += 1
            break
    if divided == 0:
        is_it = 1
    if is_it == 1:
        mth_prime += 1
print number
