# Demonstrate higher-order functions by using map() with lambda to compute the square of each list item,
# and reduce() from functools to calculate the cumulative product of the list.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

product = reduce(lambda x, y: x * y, numbers)

print("Squares:", squares)
print("Cumulative product:", product)