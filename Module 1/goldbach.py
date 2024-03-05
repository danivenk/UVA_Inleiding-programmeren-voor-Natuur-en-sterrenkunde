# Dani van Enk, 11823526
# goldbach.py maakt gebruik van de stelling van Goldbach

# variables and lists
number = 20000 #int(raw_input("geef een cijfer: "))
prime = []
even = []
# creates a list of primes up to number
for some_number in range(2, number + 1):
    devided = 0
    is_it = 0
    for another_number in range(2, some_number):
        if some_number % another_number == 0:
            devided += 1
            break
    if devided == 0:
        is_it = 1
    if is_it == 1:
        prime.append(some_number)

# creates a list of even numbers up to number
for yet_another_number in range(4, number+1):
    if yet_another_number % 2 == 0:
        even.append(yet_another_number)

# prints all even numbers in the even list and gives the sum of 2 primes (that are equal to that even number)
for even_number_in_list in range(0, len(even)):
    print even[even_number_in_list], "=",
    number_of_answers_is_1 = 1
    goldbach_wrong = 0
    for prime_1 in range(0, len(prime)):
        for prime_2 in range(0, len(prime)):
            if prime[prime_1] + prime[prime_2] == even[even_number_in_list]:
                goldbach_wrong = 1
                if prime[prime_1] <= prime[prime_2] and number_of_answers_is_1 == 1:
                    print prime[prime_1], "+", prime[prime_2]
                    number_of_answers_is_1 = 0
    # if such a sum can't be found, it prints the even number and "Bingo"
    if goldbach_wrong == 0:
        print even[even_number_in_list], "Bingo"
        break
            
