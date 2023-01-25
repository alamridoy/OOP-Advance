class Dog:
  def __init__(self,name,color) -> None:
    self.name = name
    self.__color = color
    
  def view(self):
    print(self.name,self.__color)
    self._abc()
  
  def _abc(self):  #private method
    print("Hello return")

d1 = Dog('Puppy','Black')
d2 = Dog('Bulldog','Brown')

d1.view() 