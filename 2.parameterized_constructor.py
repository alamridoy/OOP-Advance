class Student:
  def __init__(self,name,id,dep):
    self.name = name  #instance variable
    self.id = id   #instance variable
    self.dep=dep  #instance variable
    

s1 = Student('Ridoy',11660,'CSE')
s2 = Student('Riyad', 11454,'EEE')
s1.id =3333
print(s1.name, s1.id,s1.dep)
print(s2.name, s2.id, s2.dep)

