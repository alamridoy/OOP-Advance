class Data:
  def __init__(self,x):
    self.x = x
    
  def __add__(self,another):
    return self.x + another.x
  

n1 = Data(10)
n2 = Data(20)

str1 = Data('CSE')
str2 = Data('111')

print(n1 + n2)
print(str1 + str2)