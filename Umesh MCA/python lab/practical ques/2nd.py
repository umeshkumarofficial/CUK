#User enter numbers continuously & calculates their sum. the loop should terminate when user enter 0.using while loop.

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    total = total + num

print("Sum =", total)