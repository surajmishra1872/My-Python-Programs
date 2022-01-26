class A:
    def __init__(self,name,title,age):
        self.name=name
        self.title=title
        self.age=age
    def __len__(self):
        return len((self.name))
b=A("suraj","mishra",18)
print(b)
