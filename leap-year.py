'''
Logic for leap year
A year is a leap year if:
1. it is divisible by 4 and
2. it is divisible by 100, then it must be divisible by 400

Ex: 2000 -> Leap year (divisible by 400)
Ex: 1900 -> Not a leap year (divisible by 100 but not 400)
'''

year = int(input("Enter a year : "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# If year is exactly divisible by 4 and 
# year is not divisible by 100 or 
# year is exactly divisible by 400
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")