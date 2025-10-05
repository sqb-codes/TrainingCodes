# My first Python Program
# How to use Print statement ?
print("Hello world...")
print('This is my first Python program...')

a = 12
b = 33
c = a + b

print("Sum is",c)
print("Sum of",a,"and",b,"is",c)
print("Sum of %d and %d is %d"%(a,b,c))
print("Sum of {} and {} is {}".format(a,b,c))

# f-strings - recommended
print(f"Sum of {a} and {b} is {c}")

d = a - b
e = a / b
f = a * b

print(f"Sub is {a} and {b} is {d}")
print(f"Div is {a} and {b} is {e:.2f}")
#print(f"Mul is {a} and {b} is {f}")

print(f"Mul is {a} and {b} is {a * b}")

print(f"""
Sum of {a} and {b} is {c}
Sub of {a} and {b} is {d}
Div of {a} and {b} is {e:.3f}
Mul of {a} and {b} is {f}
""")
