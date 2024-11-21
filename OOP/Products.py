class Product:
    def __init__(self, product_id:int, product_name:str, quantity_in_stock:int):
        self.setProductID(product_id)
        self.setProductName(product_name)
        self.setQuantityStock(quantity_in_stock)

    def getProductID(self):
        return self.__product_id
    
    def setProductID(self,product_id: int):
        if not product_id or not isinstance(product_id,int):
           raise ValueError("Not valid product ID")
        else:
            self.__product_id=product_id

    def getProductName(self):
        return self.__product_name
    
    def setProductName(self,product_name:str):
        if not product_name or not isinstance(product_name,str):
            raise ValueError("Not valid product name")
        self.__product_name=product_name

    def getQuantityStock(self):
        return self.__quantity_in_stock
    
    def setQuantityStock(self,quantity_in_stock):
        if not quantity_in_stock or not isinstance(quantity_in_stock,int):
            raise ValueError("  ")
        self.__quantity_in_stock=quantity_in_stock
    
    def addjustQuantityInStock(self, quantity:int):
        """ In order to increase the number of items in storage pass positive number. To decrease pass negative number """
        if not quantity or not isinstance(quantity,int):
            raise ValueError("please enter valid element")
        self.__quantity_in_stock+=quantity
        

    def __str__(self) -> str:
        return f"Product ID: {self.__product_id}, Product name: {self.__product_name}, Quantity in stock: {self.__quantity_in_stock}"

def main():
     #product1
    p_id=1
    p_name="Apple"
    qnt_stock=7
    apples=Product(p_id,p_name,qnt_stock)
    print(str(apples))
    new_quantity=8
    apples.addjustQuantityInStock(new_quantity)
    #print(apples.getQuantityStock())
    print(str(apples))
   
    print("_______________________________________\n")
    
    #product2
    p_id2=2
    p_name2="Peach"
    qnt_stock2=30
    peaches=Product(p_id2,p_name2,qnt_stock2)
    print(str(peaches))
    new_quantity=-6
    peaches.addjustQuantityInStock(new_quantity)
    print(str(peaches))
    
if __name__=="__main__":
    main()
 


