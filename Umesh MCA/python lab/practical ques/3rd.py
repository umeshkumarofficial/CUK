#Program that take a non-negative integer n as input & calculates its factorial(n!) using while loops.

n = int(input("Enter a non-negative integer: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is", fact)