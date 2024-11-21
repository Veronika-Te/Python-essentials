from decimal import Decimal
class Book:
    def __init__(self,title:str,author:str, price: Decimal):
        self.setTitle(title)  
        self.setAuthor(author)
        self.setPrice(price)
    
    def getTitle(self):
        return self.__title
    
    def setTitle(self,title:str):
        if not title or not isinstance(title, str):
           raise ValueError("Not valid title")
        else:
            self.__title=title
    
    def getAuthor(self):
        return self.__author
    
    def setAuthor(self,author:str):
        if not author or not isinstance(author,str):
            raise ValueError("Not valid author's name and surname")
        else:
            self.__author=author
            
    def getPrice(self):
        return self.__price 
    
    def setPrice(self,price):
        if not price or not isinstance(price,Decimal):
           raise ValueError("Please enter correct decimal price")
        if price>10: #price cannot be set below 10
           self.__price=price
        else:
           raise ValueError("Please enter the price that is not equal 10")
    
    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Price: {self.__price}"

if __name__=="__main__":
    
    title="Order of the Phooenix"
    author="K.Rowling"
    price=Decimal(234)
    book1=Book(title, author,price)
    print(str(book1))
        
