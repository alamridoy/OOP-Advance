class Cat:
  def __init__(self,color, action) -> None:
    self.color = color
    self.action = action
    
  def view(self):
    print(self.color, 'is a cat and cat is ',self.action)
    
    
  def compare(self,c):
    if self.action == c.action:  # c1.compare(c2) => here c1(action) recived self.action and c2(action recived) c.action
      print(self.action,'and',c.action,'is maching')
      
    else:
      print('Not maching')
  
  
  
    
c1 = Cat('white','sleeping')
c2 = Cat('black','jumping')
c3 = Cat('brown','jumping')

c1.view()
c2.view()

c2.compare(c3)