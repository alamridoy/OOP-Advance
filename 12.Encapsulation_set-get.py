class Student:
  def __init__(self,name,id,university = 'DIU'):
    self.name = name
    self.__id = id
    self.university = university
    
  def view(self):
    print('Name:',self.name,'Id:',self.__id,'University:',self.university) 
  
  def set_id(self,id):
    if (id>0):
      self.__id = id
    else:
      print('Invalid Id')
    
  def get_id(self):
    return self.__id
  
  def set_name(self,name):
    self.name = name
    
  def get_name(self):
    return self.name
  
  
      
  
  
  
s1 = Student('Ridoy',660)
s2 = Student('Mehedi',1122,'AIUB')

s1.set_id(999)
s2.set_id(111)
s1.set_name('Raihan')
s2.set_name('Jamal')
s1.view()
s2.view()

