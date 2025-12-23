class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
    
  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self,value):
    if not isinstance(value, int) or value <= 0:
      raise ValueError("Define  positive value for age")
    self.__age=value
    
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value):
    if not isinstance(value, str) or not value.isalpha():
        raise ValueError("Not valid name")
    self.__name = value
    
def main()->None:  
  try:  
    name="Mary"
    #age=-23
    age=37
    p=Person(name,age)
    print(f"Name:{p.name}, Age:{p.age}")
  except ValueError as e:
    print(f"Initialization error: {e}")

if __name__=="__main__":
    main()