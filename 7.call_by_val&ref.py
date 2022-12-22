class Student:
  def __init__(self, name,roll,sub):
    self.name = name
    self.roll = roll
    self.sub = sub
    
  def view(self,roll,sub):   # roll is int its call by value   and sub is a list its call by reference
    roll += 5
    new_sub = sub
    new_sub[0]= 'CSE'
    
    print('Method inside: ',roll)
    print('Method inside: ',sub)
    

sub = ['BBA','EEE','LLB','Ar']
roll = 5

s1 = Student('Rakib',22,sub)
s1.view(roll,sub)


print(roll) # its not change bcz its call by value
print(sub) # its change bcz its call by reference