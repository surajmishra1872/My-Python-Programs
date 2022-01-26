class Person:
    def __init__(self,first_name,last_name,age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def fullname(self):
        return f"{p1.first_name}{p1.last_name}"

p1  = Person("suraj","kumar",28)

print(p1.fullname())
