class Rectangle:
  __length = 0 #private variable
  __breadth = 0#private variable
  def __init__(self): #constructor
      self.__length = 5
      self.__breadth = 3#printing values of the private variable within the class
      print(self.__length)
      print(self.__breadth)

rec = Rectangle() #object created for the class 'Rectangle'
#printing values of the private variable outside the class using the object created
#for the class 'Rectangle'
#print(rec.breadth)
