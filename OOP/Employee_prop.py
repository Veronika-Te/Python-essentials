class mydecscriptor:
    def __init__(self, fget=None, fset=None):
        self.__fget=fget
        self.__fset=fset
        
    def __get__(self, instance, owner=None):
        # print(f"self is {self}")
        # print(f"instance {instance}")
        # print(f"owner {owner}")        
      
        if instance is None:
           return self
        if owner is None:
           raise AttributeError("Nooo")
        return self.__fget(instance) 
    
    def __set__(self, instance, value):
        if self.__fset==None:
           raise AttributeError("Noooo")
        self.__fset(instance, value) 
        
    def setter(self, fn):
        self.__fset=fn
        
class Employee:
    def __init__(self,salary:float, name:str= " ")->None:
        self.salary=salary
        self.name=name
    
    @mydecscriptor
    def salary(self):
        return self.__salary

    @salary.setter
    def SetSalary(self,value:float)->None:
        if value==0:
            raise ValueError("Not valid salary")
        max_value=400000.0
        if value>0:
           if isinstance(value,float):
              if value<max_value:
                 #print("Successfully accessed")
                 self.__salary=value
              else:
                 raise ValueError("Value exceeds a predefined maximum.") 
           else:
              raise TypeError("Not valid salary")
        else:
            raise ValueError("Not valid salary")   
    

    def __str__(self)->str:
        return f"Employee: {self.name}, Salary: {self.salary}"
        
def main()->None:
    emp=Employee(23000.0, "James")
    
    #print(emp.__dict__)
    
    #emp.salary=600000.0#Error case
    emp.salary=80000.7
    print(emp)
    
if __name__=="__main__":
   main()


