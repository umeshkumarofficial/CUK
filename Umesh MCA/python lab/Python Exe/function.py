def testing(t,m):
    x = t**10 + m//5
    if(x>10):
        return(x)
    else:
        return(x*5)

a,b = 10,5
p = testing(a,b)
print(p)