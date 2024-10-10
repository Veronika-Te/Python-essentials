import abc
from decimal import Decimal
from typing import TypeVar
Order=TypeVar("Order", bound="Order")
Review=TypeVar("Review", bound="Review")

class MenuItem:
    __slots__=('__name', '__price', '__ingredients')
    def __init__(self,name:str=" ", price: Decimal=0, ingredients: list[str] = [])->None:
        self.name=name
        self.price=price
        self.ingredients=ingredients
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string")
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value>0:
           if isinstance(value, Decimal):
               self.__price=value
           else:
               raise TypeError("Invalid type for price")
        else:
            raise ValueError("Not valid price")
        
    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self,value):
        if isinstance(value,list):
           for i in value:
               if isinstance(i,str):
                   self.__ingredients=value
               else:
                   raise ValueError("Not valid ingredients")
        else:
            raise TypeError("Not valid ingredients, please provide list which contains strings")
     
    def __str__(self):
        return f"Menu item: {self.name}, Price: {round(self.price)}, \n Ingredients: {self.ingredients}\n" 

class Appetizer(MenuItem):
    __slots__=('__glutenfree')
    def __init__(self,name, price, glutenfree, ingredients)->None:
        super().__init__(name, price, ingredients)
        self.__glutenfree=glutenfree
   
    @property
    def glutenfree(self):
        return self.__glutenfree
    
    @glutenfree.setter
    def glutenfree(self, value):
        if isinstance(value,bool):
           self.__glutenfree=value
        else:
            raise TypeError("Not valid characteristic") 
        
    def __str__(self):
        return f"Appetizer item: {self.name}, Price: {round(self.price)}, Gluten free: {self.glutenfree},\n Ingredients: {self.ingredients}\n" 

class Entree(MenuItem):
    __slots__=('__vegeterian')
    def __init__(self,name, price, ingredients, vegeterian)->None:
        super().__init__(name, price, ingredients)
        self.__vegeterian=vegeterian
    @property
    def vegeterian(self):
        return self.__vegeterian
    @vegeterian.setter
    def vegeterian(self, value):
        if isinstance(value,bool):
            self.__vegeterian=value
        else:
            raise TypeError("Not valid characteristic") 
        
    def __str__(self):
        return f"Entree item: {self.name}, Price: {round(self.price)}, Vegeterian: {self.vegeterian}, Ingredients: {self.ingredients}\n" 

class Dessert(MenuItem):
    __slots__=('__sugarfree')
    def __init__(self,name, price: Decimal, ingredients, sugarfree:bool)->None:
        super().__init__(name, price, ingredients)
        self.__sugarfree=sugarfree
        
    @property
    def sugarfree(self):
        return self.__sugarfree
    @sugarfree.setter
    def sugarfree(self, value):
        if isinstance(value,bool):
            self.__sugarfree=value
        else:
            raise TypeError("Not valid characteristic")
        
    def __str__(self):
        return f"Dessert item: {self.name}, Price: {round(self.price)}, Sugarfree: {self.sugarfree}, Ingredients: {self.ingredients}\n" 

class Customer:                                                                                            
    __slots__=('__name','__email','__phonenumber', '__order_history', '__reviews') 
    
    def __init__(self,name:str=" ", email:str=" ", phonenumber = 0)->None:
        self.__name=name
        self.__email=email
        self.__phonenumber=phonenumber
        self.__order_history=[]
        self.__reviews=[]
        
    def add_to_order_history(self, order: Order)->None:
        if not order:
            raise ValueError("There is no order to add")
        else:
            self.order_history.append(order)

    def add_review(self, review):
        if isinstance(review,Review):
           self.reviews.append(review)
        else:
            raise TypeError("Not valid review to add")
               
    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string")
        
    @property
    def order_history(self):
        return self.__order_history

    @order_history.setter
    def order_history(self,value):
        if isinstance(value,list):
           for i in value:
               if isinstance(i,Order):
                   self.__order_history=value
               else:
                   raise ValueError("Not valid order history")
        else:
            raise TypeError("Not valid order history, please provide list which contains strings")
        
    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, value):
        symbol='@'
        if isinstance(value, str):
           if symbol in value:
              self.__email = value
           else:
               raise ValueError("Not valid mail")
        else:
            raise TypeError("Must be a string.")
        
    @property
    def phonenumber(self):
        return self.__phonenumber
    
    @phonenumber.setter
    def phonenumber(self, value):
        #to validate phone number
        if value>0:
           self.__phonenumber=value
        else:
            raise ValueError("Invalid phone number")
        
    @property
    def reviews(self):
        return self.__reviews
    
    @reviews.setter
    def reviews(self,value: list[Review]):
        if isinstance(value,list):
            self.__reviews=value
        else:
            raise TypeError("Not valid reviews ( must be list of Reviews)")
            
    def contact_info(self):
        return {"Email":self.email, "Phonenumber":self.phonenumber}
    
    def view_history(self):
        return f"{self.order_history}"
        
    def __str__(self)->str:
        """Return a string representation for customer"""
        return f"Customer name:{self.name}, Contact info:{self.contact_info()}" 

class Review:   
    __slots__=('__customer_name', '__order', '__rating', '__comments')
    
    def __init__(self, customer_name:str,order: Order, rating:int =0, comments:str=" ")->None: 
        self.__customer_name=customer_name
        self.__order=order
        self.__rating=rating
        self.__comments=comments
   
    @property
    def customer_name(self):
        return self.__customer_name
    
    @customer_name.setter
    def customer_name(self, value):
        if isinstance(value, str):
            self.__customer_name = value
        else:
            raise TypeError("Name must be a string")
    
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self,value):
        min_rating=0
        max_rating=10
        if min_rating<value<max_rating:
            if isinstance(value,int):
                self.__rating=value
            else:
                raise TypeError("Not valid type")
        else:
            raise ValueError("Out of boundaries")
        
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,value):
        if isinstance(value,Order):
           self.__order=value
        else:
            raise TypeError("Not valid order")
    
    @property
    def comments(self):
        return self.__comments
    
    @comments.setter
    def comments(self,value):
        if isinstance(value,str):
            self.__comments=value
        else:
            raise TypeError("not valid type")
        
    def __str__(self) -> str:
        """Return a string representation for review"""
        return f"REVIEW: Customer Name: {self.customer_name}, Rating : {self.rating}, Comments: {self.comments} for order {self.order}" 
    
class Order(abc.ABC):
      
      __slots__=('__customer', '__menu_items','_total_price','__tips') 
      
      def __init__(self, customer: Customer, menu_items: list[MenuItem], tips: Decimal = Decimal('0.0'))->None:
          self.__customer = customer 
          self.__menu_items = menu_items 
          self.__tips = tips
          self._total_price = self.calculate_total_price()
          self.customer.add_to_order_history(self)
          
     
      @abc.abstractmethod
      def calculate_total_price(self) -> float:
          """Calculate the total price of the order."""
          pass
      
      @property
      def customer(self):
          return self.__customer
      
      @customer.setter
      def customer(self,value:Customer):
          if isinstance(value,Customer):
             self.__customer=value
          else:
              raise TypeError("Not valid customer")
      
      @property
      def menu_items(self):
          return self.__menu_items
      
      @menu_items.setter
      def menu_items(self,value: list[MenuItem]):
          if isinstance(value, list):
             for i in value:
                 if isinstance(i, MenuItem):
                     self.__menu_items=value
                 else:
                     raise TypeError("Not valid menu items")
          else:
             raise TypeError("Not valid menu items")
      @property
      def tips(self):
          return self.__tips
    
      @tips.setter
      def tips(self, value):
          if isinstance(value, Decimal):
             if value >= Decimal('0.0'):
                self.__tips = value
             else:
                raise ValueError("Tips cannot be negative")
          else:
             raise TypeError("Tips must be a Decimal type")   

                        

class DineInOrder(Order):
    def calculate_total_price(self) -> float:
        """Calculates total price of products for dine in order"""
        #cast to float total price for better print
        return float(sum(item.price for item in self.menu_items ) + self.tips)
    
    def __str__(self)->str:
        return f"\nDINE IN ORDER: Name:{self.customer}, \n Ordered items: {', '.join(str(i) for i in self.menu_items)}, Total price: {self._total_price}, Tips {self.tips}"    


class TakeawayOrder(Order):
    def calculate_total_price(self) -> float:
        """Calculates total price of products for take away orders"""
        return float(sum(item.price for item in self.menu_items ))
    
    def __str__(self)->str:
        return f"\nTAKEAWAY ORDER: Name:{self.customer}, \n Ordered items: {', '.join(str(i) for i in self.menu_items)}, Total price: {self._total_price}, Tips {self.tips}" 
    
class DeliveryOrder(Order):
    def calculate_total_price(self) -> float:
        """Calculates total price of products for delivery orders"""
        return float(sum(item.price for item in self.menu_items ))
    
    def __str__(self)->str:
        return f"\nDELIVERY IN ORDER: Name:{self.customer}, \n Ordered items: {', '.join(str(i) for i in self.menu_items)}, Total price: {self._total_price}, Tips {self.tips}" 
    
def main():
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~Restaurant Menu~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    #creating menu item
    name="The Vege-Express"
    price=Decimal(17.90)
    ingredients=["vegeterian patty", "cheese", "tomato", "lettuce", "mayonnaise"]
    mi1=MenuItem(name, price, ingredients)
    print(mi1)
    mi1.ingredients
    
    #creating dessert item
    name="Strawbrry cake"
    price=Decimal(3.99)
    ingredients=["strawberry","cake"]
    sugarfree=False
    d1=Dessert(name, price,ingredients, sugarfree)
    print(d1)
    
    #creating entree
    name="Bruschetta"
    price=Decimal(1.99)
    ingredients=["tomato","basil", "grilled bread"]
    vegeterian=True
    ent1=Entree(name,price, ingredients, vegeterian)
    print(ent1)
    #ent1.name="Rice"
    
    #creating appetizer
    name="Peanut butter cookie"
    price=Decimal(1.99)
    ingredients=["peanut butter","white sugar", "egg"]
    glutenfree=False
    ap1=Appetizer(name, price, glutenfree, ingredients)
    print(ap1)
    
    #creating customer
    name="Michael"
    email="Michael.Smith@gmail.com"
    phone=199387
    cust1=Customer(name, email,phone)
    print(cust1," \n")
    
    print("___________________________Reviews___________________________")
    #creating review
    review=Review(cust1.name,7, "Delicious food")
    print(review)
    
    #Creating dine in order
    menu_items_lst=[ap1,ent1]
    tips=Decimal('3.50')
    dine=DineInOrder(cust1,menu_items_lst,tips)
    print("Dine in order")
    print(dine)
    
    #Creating takeaway in order
    menu_items_lst=[d1]
    tips=Decimal('4.50')
    take_away=TakeawayOrder(cust1,menu_items_lst,tips)
    print("Take away order")
    print(take_away)
    
    #Creating delivery order
    menu_items_lst=[ap1]
    tips=Decimal('7.50')
    delivery=DeliveryOrder(cust1,menu_items_lst,tips)
    print("Delivery order")
    print(delivery)
   
    
if __name__=="__main__":
    main()