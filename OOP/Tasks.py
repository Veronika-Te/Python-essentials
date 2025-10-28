# Create a class named Car with no methods or attributes
class CarEmpty:
  pass

# Modify Car to accept brand and model as parameters
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

#3 Extend Car by adding display_info() method
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def display_info(self):
    print(f"Car brand: {self.brand}, model: {self.model}")

# 4 Add a default value for model ("Unknown")
class Car:
  def __init__(self, brand, model="Unknown"):
    self.brand = brand
    self.model = model

  def display_info(self):
    print(f"Car brand: {self.brand}, model: {self.model}")

# 5️ Create Person class and print info of multiple instances
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 6 Create BankAccount with deposit() method
# 7 Add withdraw() method with balance check
class BankAccount:
  def __init__(self, account_number, balance=0):
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):
    if not isinstance(amount,(int,float)):
      print("Error: amount must be a number (int or float)")
      return
    self.balance += amount
    print(f"Deposited {amount}. New balance: {self.balance}")

  def withdraw(self, amount):
    if not isinstance(amount,(int,float)):
      print("Error: amount must be a number (int or float)")
      return
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdrew {amount}. New balance: {self.balance}")
    else:
      print("Insufficient funds")

# 8️ Student class with total count tracking
# 9️  Add __str__ method to Student
class Student:
  total_students = 0

  def __init__(self, name):
    self.name = name
    Student.total_students += 1

  def __str__(self):
    return f"Student name: {self.name}"

# 10 Employee class with give_raise()
class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    if not isinstance(amount,(int,float)):
      print("Error: amount must be a number (int or float)")
      return
    self.salary += amount
    print(f"{self.name} got a raise! New salary: {self.salary}")


if __name__=="__main__":
  #print its type
  car1 = CarEmpty()
  print(type(car1))  # <class '__main__.Car'>

  # Create an instance and print attributes
  car2 = Car("Alpha Romeo", "Stelvio")
  print(car2.brand)   # Alpha Romeo
  print(car2.model)   # Stelvio
  
  # Display info
  car3 = Car("Honda", "Civic")
  car3.display_info()

  # Default value
  car4 = Car("Ford")
  car4.display_info()  # Car brand: Ford, model: Unknown
  
  # People
  people=[]
  p1=Person("Alice", 25)
  p2=Person("Bob", 30)
  p3=Person("Charlie", 22)
  people.append(p1)
  people.append(p2)
  people.append(p3)

  for person in people:
      print(f"Name: {person.name}, Age: {person.age}")
      
      
  # Bank account
  account1 = BankAccount("12345", 100)
  account1.deposit(50)
  
  account2 = BankAccount("67890", 200)
  account2.withdraw(50)
  account2.withdraw(200)
  
  #Student
  s1 = Student("Anna")
  s2 = Student("Ben")
  s3 = Student("Chris")

  print(f"Total students: {Student.total_students}")
  
  s4 = Student("David")
  print(s4)
  print(f"Total students: {Student.total_students}")

  #Employee
  emp1 = Employee("Eva", 50000)
  emp1.give_raise(5000)
