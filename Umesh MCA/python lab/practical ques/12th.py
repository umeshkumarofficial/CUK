    # Write a recursive function factorial(n) that calls itself to compute the factorial of a non-negative integer n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a non-negative integer: "))

print("Factorial:", factorial(n))