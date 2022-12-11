class Car:
  def __init__(self,name,brand) -> None:
    self.name = name
    self.brand = brand
    self.num_of_wheel = 4
    
  
  def display(self):
    print('Car Name: ',self.name, 'Car Brand: ',self.brand ,'Num of car wheel: ',self.num_of_wheel)
    
car1 = Car('Prius','Toyota')
car2 = Car('Mazda rx','Mazda')
car1.display()
car2.display()