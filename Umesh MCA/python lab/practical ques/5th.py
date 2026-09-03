#Print 1 to 30 , skip any no. multiple of 3, stop loop when no is divide by 13, print all other no.

for i in range(1, 31):
    if i % 13 == 0:
        break
    elif i % 3 == 0:
        continue
    else:
        print(i)

