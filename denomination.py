'''
Logic
Input amount from user
If amount > 500, divide amount by 500
- get max 500 notes required
Store division result in some variable = n = amount / 500
After division, subtract the resultant amount of 500 notes from amount
amount = amount - (note_500 * 500)
or
amount = amount % 500
'''

amount = int(input("Enter the amount : "))
notes_of_500 = 0
notes_of_100 = 0
notes_of_50 = 0
notes_of_10 = 0
notes_of_5 = 0
notes_of_1 = 0

if amount > 500:
    notes_of_500 = amount // 500
    amount = amount % 500

if amount > 100:
    notes_of_100 = amount // 100
    amount = amount % 100

if amount > 50:
    notes_of_50 = amount // 50
    amount = amount % 50

if amount > 10:
    notes_of_10 = amount // 10
    amount = amount % 10

if amount > 5:
    notes_of_5 = amount // 5
    amount = amount % 5

if amount > 1:
    notes_of_1 = amount

print("Total number of notes :")
print(f"500 = {notes_of_500}")
print(f"100 = {notes_of_100}")
print(f"50 = {notes_of_50}")
print(f"10 = {notes_of_10}")
print(f"5 = {notes_of_5}")
print(f"1 = {notes_of_1}")