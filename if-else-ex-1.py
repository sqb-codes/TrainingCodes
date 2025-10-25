num = int(input("Enter a number: "))

# Python don't have {} support for if-else block
# Python uses colon (:) and indentation (spaces) to identify if a particular code is inside if statement or not
# Indentation will be of 4 spaces
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd")

print("This statement is outside the if block.")