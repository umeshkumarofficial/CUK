# Write a program that reads space-separated numerical input into a list, passes the list to a function, and
# calculates both the sum and average of the elements.

def calculate(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return total, average


values = input("Enter numbers separated by space: ")
numbers = list(map(int, values.split()))

total, average = calculate(numbers)

print("Sum:", total)
print("Average:", average)