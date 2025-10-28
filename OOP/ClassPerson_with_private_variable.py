class Person:
    def __init__(self,name,age):
        self.name=name
        self.setAge(age)
        
    def printInfo(self)->None:
        """Prints information about person"""
        print(f"name: {self.name},\t age: {self.__age} \n")
        
    def printGreeting(self)->None:
        """Prints greeting message"""
        print(f"Greetings {self.name}!!!")
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if not self.name or not isinstance(name, str):
            raise ValueError("Provide correct name")
        self.__name=name
    
    def getAge(self):
        return self.__age
    
    def setAge(self,value):
        print("____After calling setter____")
        if value<0 or value>110:
            raise ValueError("Provide correct age")
        self.__age=value

def main()-> None:
    
    #Mary
    try:
        name="Mary"
        age=34
        person1=Person(name, age)
        person1.printGreeting()
        person1.printInfo()
        #print(person.getAge())
        changed_age=11
        person1.setAge(changed_age)
        person1.printInfo()
    except Exception as e:
         print(f"Error with Mary: {e}")
    
    #Mark
    try:
        name="Mark"
        age=12
        person2=Person(name, age)
        person2.printGreeting()
        person2.printInfo()
        changed_age=14.5
        person2.setAge(changed_age)
        person2.printInfo()
    except Exception as e:
        print(f"Error with Mark: {e}")
        

if __name__=="__main__":  
    main()
    
        
 

