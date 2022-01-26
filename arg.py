# *args programs

def all_total(a,b,* args):
    total=0
    print(a)
    print(b)
    print(args)
   for i in args:
        total+=i
    print(total)
all_total(1,2,3,4,5)

#swap program

a=int(input("enter your first number"))
b=int(input("enter your second number"))

c=a
a=b
b=c
a,b=b,a
print(a)
print(b)

#example 2

def power(a,*args):
    for i in args:
        if i:
           return[i**a for i in args]
        else:
            "you did not pass any value"
num=[2,2,3,4]
print(power(*num))




#args as argument program

def multiply(*args):
    multi=1
    for i in args:
        multi*=i
    return multi
num=[1,2,3,4,5]
print(multiply(*num))
