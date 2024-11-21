class mydescriptor:
    def __init__(self, fget=None, fset=None):
        self.__fget=fget
        self.__fset=fset
        
    def __get__(self, instance, owner=None):
        print(f"self is {self}")
        print(f"instance {instance}")
        print(f"owner {owner}")        
      
        if instance is None:
           return self
        if owner is None:
           raise AttributeError("Nooo")
        return self.__fget(instance) 
    
    #the score is within a valid range (e.g., 0-100).
    def __set__(self, instance, value):
        print("called setter")
        if self.__fset==None:
           raise AttributeError("Noooo")
        self.__fset(instance, value) 
        
    def setter(self, fn):
        self.__fset=fn

class Student:
    def __init__(self,score:float)->None:
        self.__score=score
    
    @mydescriptor
    def score(self):
        print("getter called")
        return self.__score

    @score.setter
    def setScore(self,value:float)->None:
        if value==0:
            raise ValueError("Not valid score")
        if 0<value<100:
           if isinstance(value,int) or isinstance(value,float):
              self.__score=value
              print("Successfully accessed")
           else:
              raise ValueError("Not valid score")
        else:
            raise ValueError("Not valid score")


     
def main()->None:
    s=Student(8)
    s.score
    s.score=6 
    print(s.score)
    
if __name__=="__main__":
   main()

    