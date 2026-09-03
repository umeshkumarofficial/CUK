prime_number = [n for n in range(500, 5001) if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]

print(prime_number)




#In simple way code

""" 
prime_number = []

for n in range(500, 5001):

    if n > 1:

        is_prime = True

        for i in range(2, int(n**0.5) + 1):

            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_number.append(n)

print(prime_number)

"""