class lapton:
    def __init__(self,brand,model,price):

        self.brand = brand
        self.model = model
        self.price = price




#print(p1.model)

    def app_discount(self,num):

        d = (num//100)*self.price
        return self.price - d 
p1 = lapton("hp","32tua","20000")

print(p1.app_discount(10))
    
    

