# prime no.
# divisible by 1 and itself

# num = 17
num = 25
prime = True

# Loop from 2 to num-1
for i in range(2, num):
    if num % i == 0:
        # print("Number is not prime")
        prime = False
        break
    # else:
        # print("Number is prime")
        # prime = True

if prime:
    print("Number is prime")
else:
    print("Number is not prime")