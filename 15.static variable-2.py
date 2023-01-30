class Student:
 
  student_count = 0
  def __init__(self,name,id):
    self.name = name
    self.id = id
    Student.student_count += 1
    
  
  def details(self):
    print('name: ',self.name, 'id: ',self.id)
    

s1 = Student('Ridoy',660)
s2 = Student('Shoikot',222)
s3 = s2 = Student('Bob',926)
s1.details()
print('Total student : ', Student.student_count)



    
  