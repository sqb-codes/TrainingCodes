# num = 9945576737
num = 997
# num = 17
# num = 25
iterations = 0

for i in range(2, num//2):
    iterations += 1
    if num % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("Number of iterations:",iterations)