from typing import List
import random
import time

class Student:
    def __init__(self,name,age, grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("There is no value")
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string.")
        
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not value:
           raise ValueError("There is no value")
        if value>0 and value<120: 
           if isinstance(value, int):
              self.__age = value
           else:
               raise TypeError("Not valid type for age")
        else:
            raise ValueError("Age must be a positive integer.")
    
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if not value:
           raise ValueError("There is no value")
        if value>0 and value<=100: 
           if isinstance(value, float) or isinstance(value,int):
              self.__grade= value
           else:
               raise TypeError("Not valid type for grade")
        else:
            raise ValueError("Grade must be a positive integer (0-100).")

    def __gt__(self, other):
        """Compares students by grades"""
        if not other:
           return False
        if isinstance(other, Student):
           if self.grade>other.grade:
              return True
        else:
            return False
        
    def __repr__(self) -> str:
        """String representation"""
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}\n"
    
def insertion_sort(students: List[Student])->None:
    """Performs sorting by using insertion sort algorithm"""
    for i in range(1,len(students)):  
        key=students[i]   
        j=i-1         
        while j>=0 and students[j]>key: 
            students[j+1]=students[j]  
            j-=1 
        key, students[j+1]=students[j+1],key 

def main():  
    
    start=time.perf_counter() 
    students = [
                   
                   Student("Diana", 21, 100),
                   Student("Mark", 22, 92),
                   Student("Eve", 20, 95.2),
                   Student("Erik", 20, 86)
    ]
    print(f"Unsorted students: {students}")


    insertion_sort(students)
    end=time.perf_counter()
    print(f"\nTime for insertion sort {round(end-start,6)} seconds\n")
    print(f"Sorted : {students}")

   

if __name__=="__main__":
    main()
