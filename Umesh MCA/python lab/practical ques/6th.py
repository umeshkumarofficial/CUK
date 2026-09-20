# Write a Python program to define a function that accepts two numbers and returns their 
# addition, subtraction, and multiplication as multiplle returned values


def calculate(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y

    return addition, subtraction, multiplication


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

add, sub, mult = calculate(a, b)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mult)