from decimal import Decimal

class Employee:
    def __init__(self, employee_id:int, name:str, salary: Decimal):
        self.__employee_id=employee_id
        self.__name=name
        self.setSalary(salary) 
        
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,salary: Decimal):
        if not salary or not isinstance(salary,Decimal):
           raise ValueError("Please enter correct decimal value")
        if salary>0:
           self.__salary=salary
        else:
           raise ValueError("Please enter positive value")
    
    def __repr__(self):
        return f"Name: {self.__name}, Salary:{self.__salary}"
        
if __name__=="__main__":
    
    emp_id=1
    name="Mary"
    salary=Decimal(2334)
    emp=Employee(emp_id,name,salary )
    print(repr(emp))
            
        