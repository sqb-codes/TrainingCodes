# Operators in Python

age = int(input("Enter your age:"))
voter_id = input("Do you have voter id card : yes/no : ")

# both the condition should be true
print(age > 18 and voter_id == "yes")

# any one of the condition could be true
print(age > 18 or voter_id == "yes")

# not - Negates the condition
print(not(age > 18))

# ==================
price = 500
print("Price is :",price)

discount = 40
price -= discount
print("Price after discount :",price)

delivery_charges = 10
price += delivery_charges
print("Price after delivery charges :",price)

tax = 0.10
price += price * tax
print("Price after applying tax :",price)

print("Total Price :",price)
