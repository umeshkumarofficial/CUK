# Python script that accepts an integer  N and prints the first N numbers of the fibonacci sequence(0,1,1,2,3,5). using while loop.

n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b