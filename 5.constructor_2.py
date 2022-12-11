class Dog:
  def __init__(self,name,color) -> None:
    self.name = name
    self.color = color
    
  def update_color(self,color):
    self.color = color
    
    
  def info(self):
    print(self.color, self.name , 'is smilling')
    
d1 = Dog('Bulldog','brown')

d2 = Dog('Puppy','White')
d1.update_color('Black')
d1.info()
d2.info()

print(d1.__dict__)
print(dir(d2))