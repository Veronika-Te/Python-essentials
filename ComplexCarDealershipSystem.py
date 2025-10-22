import abc
from decimal import Decimal
import re
from typing import List, Tuple


def validate_string(value, field_name):
    """Validates string values"""
    if value is None:
        raise ValueError(f"{field_name} cannot be None")
    if not isinstance(value, str):
        raise TypeError(f"Unsupported type! {field_name} must be a string")
    if not value.replace(" ", ""):
        raise ValueError(f"{field_name} cannot be an empty or blank string")
    
def validate_int_and_range(value, field_name):
    """Validates integer values and range between 0-100"""
    if value is None:
        raise ValueError(f"{field_name} cannot be None")
    if not isinstance(value, int):
        raise TypeError(f"Unsupported type! {field_name} must be a integer")
    if not 0<=value<=100:
        raise ValueError(f"{field_name} is invalid, it must range from 0% to 100%. ")


class Car(abc.ABC):
    """Abstract class car"""
    __slots__=('__make','__model','__price')
    def __init__(self, make:str, model:str, price:Decimal)->None:
        self.make=make
        self.model=model
        self.price=price
        
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price

    @make.setter
    def make(self, value)->None:
        f_name="Make" #Field name for printing error message
        validate_string(value, f_name)
        self.__make = value
        
        
    @model.setter
    def model(self, value):
        f_name="Model"
        validate_string(value, f_name)
        self.__model = value
      
        
    @price.setter
    def price(self,value):
        f_name="Price"
        if isinstance(value, Decimal):
            if value>0:
                self.__price=value
            else:
                raise ValueError(f"{f_name} must be positive value")
        else:
            raise TypeError(f"{f_name} must be of type 'Decimal'")
    
    @abc.abstractmethod
    def __str__(self) -> str:
        """String representation"""
        return f"Make: {self.make} Model: {self.model},Price: {self.price} $ "
    
    @abc.abstractmethod
    def __repr__(self) -> str:
        pass


class ElectricCar(Car):
    """Electric Car"""
    __slots__=('__battery_capacity')
    def __init__(self, make: str, model: str, price: Decimal, battery_capacity: int) -> None:
        super().__init__(make, model, price)
        self.battery_capacity = battery_capacity
        
    @property
    def battery_capacity(self):
        return self.__battery_capacity
    
    @battery_capacity.setter
    def battery_capacity(self,value):
        f_name="Battery capacity"
        validate_int_and_range(value, f_name)
        self.__battery_capacity=value

    def __str__(self) -> str:
        """String representation"""
        return super().__str__() + f", Battery capacity {self.battery_capacity} kWh"

    def __repr__(self) -> str:
         return f" {type(self).__name__}, Make: {self.make} Model: {self.model},Price: {self.price} $, Battery_Capacity {self.battery_capacity} kWh"

class HybridCar(Car):
    
    __slots__=('__fuel_efficiency','__battery_capacity')
    def __init__(self, make: str, model: str, price: Decimal, fuel_efficiency: int, battery_capacity: int) -> None:
        super().__init__(make, model, price)
        self.fuel_efficiency = fuel_efficiency
        self.battery_capacity = battery_capacity
    
    @property
    def fuel_efficiency(self):
        return self.__fuel_efficiency
    
    @fuel_efficiency.setter
    def fuel_efficiency(self,value):
        f_name="Fuel efficiency"
        if value is None:
           raise ValueError(f"{f_name} cannot be None")
        #Hybrids are the most gasoline efficient of all cars - they typically get 48 to 60 mpg . 
        min_v=48.0
        max_v=60.0
        if isinstance(value, (float)):
            if min_v<=value <=max_v:
                self.__fuel_efficiency=value
            else:
               raise ValueError(f"{f_name} is invalid,  they typically get 48 to 60 mpg ")
        else: 
            raise TypeError(f"Unsupported type! {f_name} must be a float")
        
    
    @property
    def battery_capacity(self):
        return self.__battery_capacity
    
    @battery_capacity.setter
    def battery_capacity(self,value):
        f_name="Battery capacity"
        validate_int_and_range(value, f_name)
        self.__battery_capacity=value
           
    
    def __str__(self) -> str:
        """String representation"""
        return super().__str__() + f", Fuel efficiency {self.fuel_efficiency} mpg , Battery capacity: {self.battery_capacity} kWh"
    
    def __repr__(self) -> str:
         return f" {type(self).__name__}, Make: {self.make} Model: {self.model},Price: {self.price} $, Battery_Capacity {self.battery_capacity} kWh, Fuel efficiency {self.fuel_efficiency} mpg "
   
class SalesOperations(abc.ABC):
    @abc.abstractmethod
    def record_sale(self, tup: tuple)->None: #tuple (car,customer)
        pass

class Salespeople(SalesOperations):
    """ class Salespeople have attributes such as name and commission rate.
     Salesperson can record sale,  view their sales history and manage car inventory""" 
    def __init__(self,name:str, commision_rate:int)->None:
        self.name=name
        self.commision_rate=commision_rate
        self.__sales_history: List[Tuple[Car,Customer]]=[] # annotation list[tuple(Car,Customer)]
     
    @property
    def commision_rate(self):
         return self.__commision_rate
     
    @commision_rate.setter
    def commision_rate(self,value):
         f_name="Commision rate"
         validate_int_and_range(value, f_name)
         self.__commision_rate=value
         
    @property
    def sales_history(self):
         return self.__sales_history

    def record_sale(self, value:tuple)->None:     
        """Records sale to sales history list, as an input takes tuple with structure (car: Car, customer:Customer)"""   
        if isinstance(value,tuple):
            if len(value)==2:
                if isinstance  (value[0],Car) and isinstance(value[1], Customer):
                   self.__sales_history.append(value)
                   print(f"\n RECORD SALE INFO: Salesman: {self.name} sold {value[0].make}, {value[0].model} to {value[1].name}.")
                else:
                     raise TypeError("Unsupported type! must be (Car, Customer) pair in tuple")
            else:
               raise ValueError("Length of tuple must be 2,which includes car and customer")
        else:
                     raise TypeError("Unsupported type! must be Car, Customer pair in tuple")
     
    def view_sales_history(self)->str:
         """"Allows to view sales hisory"""
         if not self.sales_history:
            return "Empty History"
         for i in self.__sales_history:
             history=f"CAR  INFO: {str(i[0])}; CUSTOMER INFO: {str(i[1])}"
         return history
 
    def get_commission(self, car:Car):
         """Calculating commision"""
         sale_price=car.price
         commision=sale_price * Decimal(self.commision_rate/100)
         return commision
        

    def __str__(self)->str:
         """String representation"""
         return f"Name: {self.name}\n"
     
    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Dealership:
    """ class Dealership is for managing existing cars in system, and collecting informartion about salespeople"""
    
    def __init__(self)->None:
        self.__inventory: List[Car] = []
        self.__salespeople: List[Salespeople]= []

    @property
    def inventory(self):
        return self.__inventory
     
    @property
    def salespeople(self):
        return self.__salespeople
     
    def add_sales_people(self, salesperson: Salespeople):
         """Add salespeople to list"""
         if not salesperson:
            raise ValueError("Empty salesperson")
         if isinstance(salesperson, Salespeople):
             self.salespeople.append(salesperson)
         else:
             raise TypeError("Invalid type for salesperson")
         

    def add_car_inventory(self, car:Car)->None:
         """Add car to inventory list"""
         if not car:
            raise ValueError("There is no car to add")
         if isinstance(car, Car):
            self.inventory.append(car)
         else:
             raise TypeError("Invalid type for salesperson")
         
     
    def search_car(self, make=None, model=None)->List:
        """Searching for car based on names make and model"""
        results = []
        for car in self.inventory:
            if (make is None or car.make == make) and (model is None or car.model == model):
                results.append(car)
        return results  
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}"
    
class CarOperations(abc.ABC):
    @abc.abstractmethod
    def search_cars(self, dealership, make=None, model=None):
        pass
    @abc.abstractmethod
    def purchase_car(self, dealership:Dealership, car:Car, salesperson:Salespeople)->None:
        pass
    
class Customer(CarOperations):                                                                                           
    def __init__(self,name:str, email:str, phonenumber:str)->None:
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
     
    @property
    def phonenumber(self):
        return self.__phonenumber
    
    @name.setter
    def name(self, value)->None:
        f_name="Name"
        validate_string(value, f_name)
        self.__name = value
        
    @email.setter
    def email(self, value:str)->None:
         valid = re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value)
         if valid:
            #print("Valid email address.")
            self.__email = value
         else: 
             raise ValueError("Email is invalid")
  
    @phonenumber.setter
    def phonenumber(self, value):      
         if not value:
            raise ValueError("Phone number is invalid")
         
         #removing  spaces
         phonenumber=value.replace(" ", "")
        
         #Define the regular expression pattern for Armenian phone numbers
         pattern = r"^(0\d{8}|\+374\d{8})$"
        
         #Match against the pattern
         if re.fullmatch(pattern, value):
            self.__phonenumber = value
         else:
            raise ValueError("Invalid phone number")
    
    def contact_info(self):
         """Gets contact info"""
         return {"Email":self.email, "Phonenumber":self.phonenumber}
     
    def search_cars(self, dealership, make=None, model=None):
        """Searching for car in dealership inventory"""
        results = dealership.search_car(make, model)
        if results:
            print(f"Search Results for {self.name}:")
            for car in results:
                print(car)
        else:
            print(f"No cars found for {self.name}.")
            
    def purchase_car(self, dealership:Dealership, car:Car, salesperson:Salespeople)->None:
        """Purchasing car"""    
        if car in dealership.inventory:
            #removing from inventory   
            dealership.inventory.remove(car)
            #recording sale for salespeson
            tup=(car, self)
            salesperson.record_sale(tup)
            commission=salesperson.get_commission(car)
            #rounding commission for better view in cmd
            print(f"PURCHASE INFO: {self.name} purchased CAR: {car}.\n COMMISSION : Salesperson {salesperson} gets {round(commission)} $ from the sale deal")
        else:
            print(f"{car} is not available for purchase.")
            

    def __str__(self):
         """String representation"""    
         return f"Name: {self.name}"
     
    def __repr__(self) -> str:
        return f"{type(self).__name__}"
         
def main():
    try:
        dealership = Dealership()
        print("______________CARS______________\n")
        #constructing Electic Car
        #make="      " error check
        make="Tesla"
        model="Model S"
        battery=78
        p=Decimal(11000)
        c1_elect=ElectricCar(make,model,p,battery)
        print(c1_elect)
    
        #constructing Hybrid Car
        #make="      " error check
        make="Toyota"
        model="Prius"
        battery=78
        fuel=56.7
        p=Decimal(17300)
        c2_hyb=HybridCar(make,model,p,fuel,battery)
        print(c2_hyb)
        print("_____________________________")

        dealership.inventory.append(c1_elect)
        dealership.inventory.append(c2_hyb)

        #constructing Customer
        name="Mark"
        email="marksmith@gmail.com"
        phonenumber="+37499898989"
        cust1=Customer(name,email, phonenumber)
    
        #constructing Salespeople
        name="Anatoliy"
        com_rate=29
        sp=Salespeople(name, com_rate)
        #print(sp)
    
        name2="Christina"
        com_rate2=28
        sp2=Salespeople(name2, com_rate2)
    
        dealership.salespeople.append(sp)
        dealership.salespeople.append(sp2)

        #adding record sale
        tup=(c2_hyb, cust1)
        sp.record_sale(tup)
    
        print("\n________Sales history________\n")
        history=sp.view_sales_history()
        print(f"Salesman {sp} \n {history}")
    
        #Purchasing
        cust1.purchase_car(dealership,c2_hyb, sp)
        
    except Exception as e:
        print(e)
    
    
if __name__=="__main__":
    main()
   





