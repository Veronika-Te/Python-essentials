class ShoppingListBase:
  def __init__(self):
    self.items=[]
    
  def add_items(self,item: str):
    """Add an item to the shopping list and confirms the addition."""
    if not isinstance(item,str) or not item:
      return "Error : Item must be a string"
    self.items.append(item)
    print(f"Item: {item} was added to the shopping list")
    return self.items
    
    
  def remove_item(self, item:str):
    """Remove an item if it exists; otherwise, notifies the user."""
    if not isinstance(item,str) or not item:
      return "Error : Item must be a string"
    if item in self.items:
      self.items.remove(item)
      print(f"Item '{item}' was removed from the shopping list")
    else:
      return "Item was not found in the shopping list"
    
    
  def view_list(self):
    """Displays all items in the shopping list or informs if it is empty."""
    if not self.items:
      return "No item in the shopping list"
    print("Items in the shopping list")
    for item in self.items:
      print(f"{item}")

class ShoppingListWithCategories(ShoppingListBase):
  def __init__(self):
    super().__init__()
    self.categories={}
    
  def add_items(self, item:str, category:str):
    """ Adds an item to the shopping list by category"""
    if not isinstance(item,str) or not item:
      return "Error : Item must be a string"
    if not isinstance(category,str) or not category:
      return "Error : Category must be a string"
    
    super().add_items(item)
    if category not in self.categories:
      self.categories[category]=[]
    self.categories[category].append(item)
  
  def view_items(self):
    """Display items grouped by category."""
    if not self.categories:
      print("No items or categories yet.")
      return
    for category,items in self.categories.items():
      print(f"{category}: {items}")
      
  def remove_item(self, item:str):
    """Remove an item from its category."""
    if not isinstance(item,str) or not item:
      return "Error : Item must be a string"
    for products in self.categories.values():
      #print(type(products))
      if item in products:
        products.remove(item)
        print(f"Item '{item}' was removed from the shopping list")
        return
  
    return f"Error: {item} was not found in the shopping list"
      
def main():
  print("_____The shopping list_____")
  shp_list1=ShoppingListBase()
  shp_list1.add_items("product_1")
  shp_list1.add_items("product_2")
  shp_list1.add_items("product_3")
  shp_list1.add_items("product_4")
  shp_list1.add_items("product_5")
  shp_list1.view_list()
  print("After removing product_4")
  shp_list1.remove_item("product_4")
  shp_list1.view_list()
  
  shp_list_categorized=ShoppingListWithCategories()
  shp_list_categorized.add_items("product1", "category1")
  shp_list_categorized.add_items("product2", "category2")
  shp_list_categorized.view_items()
  shp_list_categorized.remove_item("product1")
  shp_list_categorized.view_items()
  
if __name__=="__main__":
  main()
