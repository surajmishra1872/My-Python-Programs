
#multilevel inheritence


class Phone:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def full_name(self):
        return(f"{self.brand_name}\n{self.model_name}")
class Smartphone(Phone):
    def __init__(self,brand_name,model_name,price,rear_camera,front_camera):
        super().__init__(brand_name,model_name,price)
        self.rear_camera=rear_camera
        self.front_camera=front_camera
    def full_name(self):
        return(f"{self.brand_name}\n{self.model_name}")
        
class Featurephone(Smartphone):
    
    def __init__(self,brand_name,model_name,price,rear_camera,front_camera,battery):
        super().__init__(brand_name,model_name,price,rear_camera,front_camera)
        self.battery=battery
    def full_name(self):
        return(f"{self.brand_name}\n{self.model_name}")
    
phone=Phone("nokia","1100",1200)
    
featurephone=Featurephone("apple","11100",1200,"12mp","20mp","4000mah")
print(featurephone.full_name())
print(help(Smartphone))
print(isinstance(featurephone,Featurephone))
print(issubclass(Featurephone,Smartphone))


#multiple class


class A:
   
    def full_name(self):
        return "hello from A"

class B:
    
    def full_name(self):
        return "hello from class B"
    

class C(A,B):
    pass
d=B()
print(d.full_name())


























