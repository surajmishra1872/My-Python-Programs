def name(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    a=odd.extend(even)
    print(a) 

num=[1,2,3,4,5,6,7,8,9,10]
print(name(num))
        
 
