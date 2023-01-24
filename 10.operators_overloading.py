# class Data:
#   def __init__(self,x):
#     self.x = x
    
#   def __add__(self,another):
#     return self.x + another.x
  

# n1 = Data(10)
# n2 = Data(20)

# str1 = Data('CSE')
# str2 = Data('111')

# print(n1 + n2)
# print(str1 + str2)


class House:
  def __init__(self, window,door):
    self.window = window
    self.door = door
  
  
  def __add__(self,other):
    return self.window + other.window, self.door + other.door
  
   
  def view(self):
    print(self.window,'windows in this house and ',self.door,'doors in this house')
    
h1 = House(6,2)
h2 = House(9,3)

print(h1.window + h2.window)
print(h1.door + h2.door)
