class Shape:#protected variables
    _length = 10 
    _breadth = 20

class Circle(Shape):
    def __init__(self):#printing protected variables in the derived class
        print(self._length)
        print(self._breadth)

cr = Circle()
#printing protected variables outsidethe class 'Shape' in which they are defined
print(cr.length)
print(cr.breadth)

