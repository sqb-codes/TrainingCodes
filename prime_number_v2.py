# prime no.
# divisible by 1 and itself

# num = 17
num = 25

# Loop from 2 to num-1
for i in range(2, num):
    if num % i == 0:
        print("Number is not prime")
        break
# This else block will execute only when loop is executed successfully
# This is known as for...else
else:
    print("Number is prime")