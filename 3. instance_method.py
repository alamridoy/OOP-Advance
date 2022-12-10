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
    


