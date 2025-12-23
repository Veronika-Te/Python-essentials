class Person:
    def __init__(self,name,age):
        self.name=name
        self.setAge(age) 
        
    def printInfo(self)->None:
        """Prints information about person"""
        print(f"name: {self.name}, age: {self.age} \n")
        
    def printGreeting(self)->None:
        """Prints greeting message"""
        print(f"Greetings {self.name}!!!")
    
    def getAge(self):
        """Getter to get age"""
        return self.age
    
    def setAge(self,value):
        """Setter to set age"""
        if value<0 or value>110:
            raise ValueError("Provide correct age")
        self.age=value

def main()-> None:
    try:
        #Mary
        name="Mary"
        age=34
        person1=Person(name, age)
        person1.printGreeting()

        #Mark
        name="Mark"
        age=12
        person2=Person(name, age)
        changed_age=12.5

    except ValueError as e:
        print("Error:", e)
    finally:
        person1.printInfo()

if __name__=="__main__":  
    main()
