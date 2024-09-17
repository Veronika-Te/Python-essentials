#Design a class ShoppingCart that encapsulates a private list of items (items).
#Implement methods to add an item, remove an item, and display the total number of items in the cart. Each item should have a name and price.

from decimal import Decimal
class ShoppingCart:   
   def __init__(self, items=None):
        self.setItem([items])
           
   def getItem(self):
       return self.__items
   
   def setItem(self,items):
       if items is None:
           self.__items=[]
       if not items or not isinstance(items,list):
           raise ValueError("Empty item")
       else:
           self.__items=[items]
       
   def add(self, items_to_add):
       """Adds an item to the cart."""
       if not items_to_add or not isinstance(items_to_add,Item):
          raise ValueError("Empty item")
       self.__items.append(items_to_add)

   def __str__(self):
       if not self.__items:
          return "Shopping cart is empty"

       items_str="\n".join(str(item) for item in self.__items)
       return f"Shopping cart:\n{items_str}"
       
  
   def remove_item(self, name):
        """Removes the first occurrence of an item from the cart by name."""
        if not name or name is None:
           raise ValueError("item to remove is empty")
        for item in self.__items:
            if item == name:
               self.__items.remove(item)
               print(f"Removed '{name}' from the cart.")
               return
        print(f"Item '{name}' not found in the cart.")    
        
   def display_shoppingcart(self):
       """Displays a total number of items"""
       return len(self.__items)
           
       
       

class Item:
    def __init__(self,name:str, price:Decimal):
        self.setName(name)
        self.setPrice(price)
        
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def setName(self,name):
        if not name or not isinstance(name,str):
            raise ValueError("Not valid item's name")
        else:
            self.__name=name
            
    def setPrice(self,price):
        if not price or not isinstance(price,Decimal):
            raise ValueError("Not valid price value")
        else:
            self.__price=price
    

    def __str__(self):
        if not self.__name or not self.__price:
            return f"Not valid item"
        return f"{self.__name}: {self.__price}"
 
def main():
    
    #Creating items
    price1=Decimal(5)
    price2=Decimal(4)
    price3=Decimal(78)
    item1=Item("item1", price1)
    item2=Item("item2",price2)
    item3=Item("item3",price3)
    
    #Creating shopping cart
    cart=ShoppingCart()
    
    cart.add(item1)
    cart.add(item2)
    cart.add(item3)
    print(str(cart))
   #Removing item
    cart.remove_item(item2)
    print(str(cart))
    #Display total number
    total_number=cart.display_shoppingcart()
    print(f"Items count in the list: ",total_number)
    
if __name__=="__main__":
    main()