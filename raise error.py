class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError
    ("suraj")

class Dog(Animal):
    def __init__(self,name,beerd):
        super().__init__(name)
        self.beerd=beerd
        

class Cat(Animal):
    def __init__(self,name,beerd):
        super().__init__(name)
        self.beerd=beerd
        
        
cat=Cat("luci","pusi")
print(cat.sound())
