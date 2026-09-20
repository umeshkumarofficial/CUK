# Write a program using an anonymous lambda function along with Python's built-in filter() to extract
# even numbers from a given list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)