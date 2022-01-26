a,b=input("enter your four number with comma sep").split(",")
a=int(a)
b=int(b)
##c=int(c)
##d=int(d)
##sqr.append(int(a**2))
##sqr.append(int(b**2))
##sqr.append(int(c**2))
num=list(range(a,b))
##sqr.append(int(d**2))
##print(sqr)
##
print(num)
num1=[]
for i in num:
    num1.append(i**2)
print(f"sqr is{num1}")
