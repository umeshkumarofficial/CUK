# Write a python function using variable length arguments(*args) to calculate the total sum of an arbitrary number of
# numerical inputs passed during a function call.


def total_sum(*args):
    total = 0

    for i in args:
        total = total + i

    return total


print("Total:", total_sum(10, 20, 30))
print("Total:", total_sum(5, 10, 15, 20, 25))