class phone:
    def __init__(self,brand_name,model_name,_price):
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = max(price,0)
        self.complete_name = f"{brand_name},{model_name},{price}"

    #def complete_name(self):
        #return self.complete_name
    

ph1 = phone("nokia","nokia1100","2000")

ph1.price = 500

print(ph1.complete_name)
print(ph1.model_name)



