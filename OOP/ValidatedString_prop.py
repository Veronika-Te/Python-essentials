class ValidatedString:
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

class User:
    def __init__(self,username:str)->None:
        self.__username=username
    
    @ValidatedString
    def username(self):
        return self.__username

    @username.setter
    def setUsername(self,value:str)->None:
        if value==0:
            raise ValueError("Not valid username")
        
        if isinstance(value,str):
           if len(value)>3:
              #print("Successfully accessed")
              self.__username=value
           else:
              raise ValueError("Not valid username")
        else:
            raise TypeError("Not valid username")     
        
def main()->None:
    u=User("user1")
    #u.username
    print(u.__dict__)
    #u.username=8 Error case
    u.username="James"
    print(u.username)
    
if __name__=="__main__":
   main()

    


