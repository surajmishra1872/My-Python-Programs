##class Laptop:
##    def __init__(self,brand_name,model_name,price):
##        self.brand_name=brand_name
##        self.model_name=model_name
##        self.price=price
##    def apply_discount(self,num):
##        disc=num*self.price/100
##        return self.price-disc
##laptop1=Laptop("hp","du1223",100000)
###laptop1.discount=50
##
##print(laptop1.apply_discount(75))
##    

class Person:
    num=0
    def __init__(self,first_name,last_name,age):
        Person.num+=1
    self.first_name=first_name
    self.last_name=last_name
    self.age=age
    
p1=Person("suraj","mishra",12)
print(Person.num)
    
