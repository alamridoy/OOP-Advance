class Student:
  def __init__(self,name,id,university = 'DIU'):
    self.name = name
    self.__id = id
    self.university = university
    
  def view(self):
    print('Name:',self.name,'Id:',self.__id,'University:',self.university)
    
  
  def update_id(self,id):
    if (id > 0):
      self.__id = id
    else:
      print('Invalid id !Please try again..')
      
  
  
  
s1 = Student('Ridoy',660)
s2 = Student('Mehedi',1122,'AIUB')

s1.update_id(999)
s1.view()
s2.view()
