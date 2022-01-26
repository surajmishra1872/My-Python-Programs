from functools import wraps
import time
def decorater_func(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print(f"function name is{func.__name__}")
        t1=time.time()
        return_valus=func(*args,**kwargs)
        t2=time.time()
        total_time = t2-t1
        print(f"total times is{total_time}")
        return return_valus
    return wrapper_func

@decorater_func
def fun(n):
    return[i**2 for i in range(1,n+1)]

print(fun(10000))
    
