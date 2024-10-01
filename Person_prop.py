class Person:
    def __init__(self, name:str, age:int)->None:
        self.name=name
        self.age=age
    
    @property
    def age(self)->int:
        return self.__age
    
    @age.setter
    def age(self,value):
        if not value or not value>0:
           raise ValueError("Define positive value for age")
        if isinstance(value,int): 
           self.__age=value
        else:
           raise ValueError("Define positive value for age")
      
    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self, value):
        if not value:
           raise ValueError("Please, define valid name")
        if isinstance(value,str):
           if value.isalpha():
               self.__name=value
           else:
               raise ValueError("Not valid name")
        else:
               raise ValueError("Not valid name")
    
def main()->None:    
    name="Mary"
    age=-23
    p=Person(name,age)
    print(f"Name:{p.name}, Age:{p.age}")
    new_age=35
    p.age=new_age 
    #p.age=-7
    
    p.name="James"
    #p.name="J7a"
    print(f"Name:{p.name}, Age:{p.age}")

if __name__=="__main__":
    main()   
