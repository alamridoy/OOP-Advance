class Book:
  def __init__(self,name,author) -> None:
    self.name = name
    self.author = author
    self.price = 0
    
  def set_price(self,price):
    self.price = price
    
  def get_price(self):
    return self.price
  
  def details(self):
    print('Book: ',self.name,
          'Author: ',self.author,
          'Price: ',self.price,'Taka')
    
b1 = Book('Opekkha','Humayan Ahmed')
b1.set_price(299)
b1.details()

b2 = Book('Horror','James')
b2.set_price(880)
b2.details()