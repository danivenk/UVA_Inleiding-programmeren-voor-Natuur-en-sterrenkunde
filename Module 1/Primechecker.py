n = int(raw_input("Prime Checker "))
# def prime_checker(ko):
#     for i in range(2, ko):
#         if ko % i == 0:
#             return False
#     return True

# for n in range(2, 1000):
o = 0
j = False
for i in range(2, n):
    if n % i == 0:
        o += 1
if o == 0:
    j = True
if j:
    print n
