##a=input("enter a number:")
##total=0
##i=0
##for i in a:
##    total+=int(i)
##print(total)
##
##move()
##print("hello")

##def num_to_string(l):
##    return[str(i) for i in l if(type(i)==int or type(i)==float)]
##print(num_to_string([True,False,[1,2,3],1,1.0,3]))

##def func(**kwargs):
##    print(kwargs)
##func(name='suraj',title='mishra')

def func(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return "not found"
            
print(func(['shivay','singh','mishra','suraj','polytechnic'],'uraj'))
