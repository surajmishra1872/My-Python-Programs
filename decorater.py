##import time
##
##def outer_function(func):
##    def inner_function():
##        print(f"this is \n{func.__name__}")
##        t1=time.time()
##        func()
##        t2=time.time()
##        t=t2-t1
##        print(f"time is{t}")
##    return inner_function()
##
##def function():
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj"
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##    print("suraj")
##
##outer_function(function)


#only int data type input program

##def only_int(function):
##    def wrapper_function(*args,**kwargs):
##        if all([type(arg)==int for arg in args]):
##            return function(*args,**kwargs)
##        print("invalid input")
##    return wrapper_function
##@only_int
##def sqr(*args):
##    total=0
##    for i in args:
##        total+=i
##    return total
##print(sqr(3,2))



