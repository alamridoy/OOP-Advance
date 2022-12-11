class Student:
  def __init__(self,name,id,dep):
    self.name = name  #instance variable
    self.id = id   #instance variable
    self.dep=dep  #instance variable
    
  def display(self): #instance method
    print('Name:',self.name,'Id:',self.id,'Department:',self.dep)
    
  
s1 = Student('Ridoy',11660,'CSE')
s2 = Student('Riyad', 11454,'EEE')

s1.display()
    


class House:
  def __init__(self) -> None:
    self.window = 4
    self.door = 1
    
  def view(self):
    print('window',self.window, 'Door', self.door)
    
obj1 = House()
obj2 = House()

obj1.window = 5
obj1.view()
obj2.view()

