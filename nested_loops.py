# Nested loops in Python
# tabular - excel - rows and cols
# 1D, 2D

# 5 x 5
"""
i = 0, j = 0,1,2,3,4
i = 1, j = 0,1,2,3,4
i = 2, j = 0,1,2,3,4
i = 3, j = 0,1,2,3,4
i = 4, j = 0,1,2,3,4
"""
# for each iteration of i, j will execute 5 times
for i in range(5): # 0,1,2,3,4
    print(f"I = {i},", end="")
    print("J = ", end="")
    for j in range(5): # 0,1,2,3,4
        print(f"{j},", end="")
    print()

print("="*20)

# Pattern Programs in Python
# *
# **
# ***
# ****
# *****
for i in range(1,5+1):
    print("*" * i)

print("=" * 20)

# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    print("*" * i)

print("+" * 20)

# Right Aligned Triangle
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,5+1):
    print(" " * (5 - i) + "*" * i)

print("+" * 20)

# Pyramid
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1,5+1):
    print(" " * (5 - i) + "*" * (2*i - 1))

print("+" * 20)

# Inverted Pyramid
# *********
#  *******
#   *****
#    ***
#     *
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2*i - 1))


# Diamond
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
for i in range(1,5+1):
    print(" " * (5 - i) + "*" * (2*i - 1))

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2*i - 1))

print("+" * 20)

# Number star triangle
# 1
# 12
# 123
# 1234
# 12345
# ith loop - number of rows
for i in range(5): # i = 0, 1, 2, 3, 4
    for j in range(i+1):  # j = i + 1
        print(j+1, end="")
    print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(5): # i = 0, 1, 2, 3, 4
    for j in range(i+1):  # j = i + 1
        print(i+1, end=" ")
    print()

print("*" * 30)

# Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
k = 0
for i in range(4): # i = 0, 1, 2, 3
    for j in range(i+1):  # j = i + 1
        k += 1
        print(k, end=" ")
    print()

print("*" * 30)

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5): # i = 0, 1, 2, 3, 4
    for j in range(5-i):  # j = i + 1
        print(j+1, end=" ")
    print()


#     1
#    12
#   123
#  1234
# 12345


#     1
#    121
#   12321
#  1234321
# 123454321


# Hollow square
# 11111
# 1   1
# 1   1
# 1   1
# 11111

