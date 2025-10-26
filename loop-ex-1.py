num = 5

# print(f"{num} x {1} = {num * 1}")
# print(f"{num} x {2} = {num * 2}")
# print(f"{num} x {3} = {num * 3}")
# print(f"{num} x {4} = {num * 4}")
# print(f"{num} x {5} = {num * 5}")
# print(f"{num} x {6} = {num * 6}")
# print(f"{num} x {7} = {num * 7}")
# print(f"{num} x {8} = {num * 8}")
# print(f"{num} x {9} = {num * 9}")
# print(f"{num} x {10} = {num * 10}")

# Syntax of a for loop
# 0,1,2,3,4
# start = 0
# stop = 5, loop will run till n-1
for i in range(5):
    print(i,end=',')

print()
print("*" * 20)

# 2,3,4,5,6,7,8,9,10
# start = 2
# stop = 11, loop will run till n-1
for i in range(2,11):
    print(i, end=',')

print()
print("*" * 20)

# 2,4,6,8,10
# start = 2
# stop = 11
# step = 2
for i in range(2,11,2):
    print(i, end=',')

print()
print("*" * 20)

# Multiplication table of a num
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")