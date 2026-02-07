num = 9945576737
# num = 997
# num = 17
# num = 25
iterations = 0

if num % 2 == 0 or num % 3 == 0:
    print("Number is not prime")
    exit()

for i in range(5, num//2, 6):
    iterations += 1
    # i = 5, 5 and 7
    # i = 11, 11 and 13
    if num % i == 0 or num % (i + 2) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("Number of iterations:",iterations)