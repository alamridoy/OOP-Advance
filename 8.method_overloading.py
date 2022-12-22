#-------------Normal way----------------

# class Calculate:
  
#   def mynum(self,num1,num2,num3): #process 1
#     if num1 != None and  num2 != None and  num3 != None :
#       print(num1*num2*num3)
#     elif  num1 != None and  num2 != None:
#       print(num1*num2)
#     else:
#       print(num1)
  
  
#   def mynum(self, *nums):  # process 2
#     sum =1
#     for num in nums:
#       sum =sum * num
#     print(sum)
    
# c1 = Calculate()
# c1.mynum(3,5,3)


#-------------Normal way----------------


from multipledispatch import dispatch

class Calculate:
  
  @dispatch(int) 
  def mynumber(self,num1):
    print(num1)
    
  @dispatch(int,int)
  def mynumber(self,num1,num2):
    print(num1*num2)
    
    
  @dispatch(str,int)
  def mynumber(self,num1,num2):
    print(int(num1)*num2)
    
  @dispatch(int,int,int)
  def mynumber(self,num1,num2,num3):
    print(num1*num2*num3)
    
    
  @dispatch(float,float,float)
  def mynumber(self,num1,num2,num3):
    print(num1*num2*num3)
    
c1 = Calculate()
c2 = Calculate()
c1.mynumber(3,2,2)
c2.mynumber(3.0,2.0,19.0)
c1.mynumber('2',5)