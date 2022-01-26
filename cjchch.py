def square(a):
     return a**2
l=[1,2,3,4,5]

def my_map(func , l):
    new=[]

    for i in l:
        new.append (func(i))
    return new
print(my_map(square , l))
    
     
