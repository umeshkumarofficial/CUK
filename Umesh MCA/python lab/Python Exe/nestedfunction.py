def sumdo(a,b):
    if(a>b):
        return(a)
    else:
        return(b)

def testing(x,y):
        return(x*y)
t = sumdo(100,200)
print(testing(t, t*2))
Ans2 = testing(sumdo(5,10), sumdo(2,3))
print(Ans2)
    