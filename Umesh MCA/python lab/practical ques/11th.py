# Construct a Python program utilizing list comprehension to iterate through a range of numbers and
# construct a list consisting only of even values.

numbers = range(1, 11)

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)