class Employee:
  def __init__(self,**kwargs):
    if len(kwargs) == 3:
      self.name = kwargs['name']
      self.id = kwargs['id']
      self.address = kwargs['address']
    
    elif len(kwargs) == 2:
      self.name = kwargs['name']
      self.id = kwargs['id']
      
      
    elif len(kwargs) == 1:
      self.name = kwargs['name']
      
    print('Object is created')
    
  
    
e1 = Employee(name = 'Rakib',id = 101)
e2 = Employee(name='Hasan',id = 222,address='Dhaka')
e3 = Employee(name='Ridoy')
     

print(e1.name)
print(e2.name, e2.id)