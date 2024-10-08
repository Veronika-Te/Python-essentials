class Person:
    __slots__=('__name', '__age', '__email')

    def __init__(self,name:str=" ", age: int=0, email:str=" ")->None:
        self.__name=name
        self.__age=age
        self.__email=email
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string.")
        
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be a positive integer.")
        
    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, value):
        symbol='@'
        if isinstance(value, str):
           if symbol in value:
              self.__email = value
           else:
               raise ValueError("Not valid mail")
        else:
            raise TypeError("Must be a string.")
    
        
    def __str__(self):
        return f"\nName: {self.name}, Age: {self.age},\nEmail:{self.email}"

def main()->None:
    p1=Person("Mary",27,"mary_janes@gmail.com")
    print(p1)
    p1.name="James"
    p1.age=45
    p1.email="james_smith32@gmail.com"
    print(p1)
    #p1.id=1 #'Person' object has no attribute 'id'
    
if __name__ =="__main__":
   main() 
   