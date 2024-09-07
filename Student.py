import statistics
class Student:
    def __init__(self,name:str,roll_number:int,grades: list):
        self.setName(name)
        self.setRollnumber(roll_number)
        self.setGrades(grades)
      
    def getName(self):
        return self.__name
    
    def setName(self,name:str):
        if not name or not isinstance(name, str):
           raise ValueError("Not valid name of student")
        else:
            self.__name=name
    
    def getRollnumber(self):
        return self.__rollnumber
    
    def setRollnumber(self,rollnumber: int):
        if not rollnumber or not isinstance(rollnumber,int):
            raise ValueError("Not valid roll number")
        else:
            self.__rollnumber=rollnumber
            
    def getGrades(self):
        return self.__grades
    
    def setGrades(self,grades: list):
        for arg in grades:
            if not isinstance(arg, int):
               raise ValueError("Please enter valid grades")
            if arg>100 or arg<0:
               raise ValueError("Please enter valid grades")
        self.__grades=grades
                    
    
    def calculate_avg(self):
        return statistics.mean(self.__grades) 
    
    def addGrades(self, ele:int):
        if not ele or not isinstance(ele,int):
           raise ValueError("please enter valid element")
        self.__grades.append(ele)
       # print("ok")
    
    def __str__(self):
        return f"Student:{self.__name}, RollNumber:{self.__rollnumber}, Grades:{self.__grades}"
    
if __name__=="__main__":
   
   name="Syuzan"
   roll_num=1
   grades=[1,2,3,99]
   stu=Student(name, roll_num,grades)
   print(str(stu))
   
   #calculate average
   res=stu.calculate_avg()
   print(f"Average of grades:{res}")
   
   stu.addGrades(7)
   print(stu.getGrades())