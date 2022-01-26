##def even_generator(n):
##    for num in range(n,n+1):
##        if num % 2 == 0:
##            yield (num)
##
##           
##for num in even_generator(20):
##    print(num



sqr =(i**2 for i in range (1,11))
for num in sqr:
    print(num)
