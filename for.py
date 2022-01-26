def gretest(a,b,c):
    if a>b and a>c:
         return c
    elif b>a and b>c:
        return c
    else:
        return c


        
a,b,c = input("enter your number").split(",")
bigger = gretest(a,b,c)
print(bigger)
