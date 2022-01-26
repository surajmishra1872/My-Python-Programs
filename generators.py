##def gen(n):
##    for i in range(1,n+1):
##        
##        yield(i)
##        
##num=gen(10)
##    
##for j in num:
##    print(j)
##for j in num:
##    print(j)
import time
t1=time.time()
l1=(i**2 for i in range(10000000))
t2=time.time()
print(t2-t1)
