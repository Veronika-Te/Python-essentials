from decimal import Decimal

#VAT rate=tax rate
def calculate_tax_rate(VAT):
    """Divides tax percentage by 100 to get tax rate as a decimal"""
    if not VAT:
       return 0
    tax_rate = Decimal(VAT/100)
    print(type(tax_rate))
    return tax_rate
   

#Original price * VAT rate=VAT amount
#Original price + VAT amount= Total price
#Original price=Unit Price
#Total price=price_with_tax

def calculate_vat_amount(unit_price, *, tax_rate=0):
    """Calculates VAT amount"""
    if not unit_price or not tax_rate:
       return 0
    return Decimal(unit_price * tax_rate) #vat amount
   
def calculate_price_with_tax(unit_price, /, vat_amount):
    """ Calculates unit price(with tax)"""
    if not unit_price or not vat_amount:
       return 0
    elif Decimal(vat_amount):
       return Decimal(unit_price + vat_amount)  #unit price with tax

def createdict(lst_keys,lst_values):
    """Creates a dictionary for product"""
    if not lst_keys or not lst_values:
        return 0
    return dict(zip(lst_keys,lst_values))

def add(*args):
    """Adds products to the shopping cart"""
    if not args:
        return 0
    shopping_cart=[]
    for i in args:
        shopping_cart.append(i)
    return shopping_cart

def calculate_total_price_shopping_cart(shopping_cart):
    """Calculates the total price of items in a shopping cart"""
    if not shopping_cart:
       return 0
    total_price_shopping=0
    for i in shopping_cart:
        total_price_shopping+=i["unit_price"]
    return total_price_shopping

def unpack_product_info(**kwargs):
    """Unpacks information about the product"""
    if not kwargs:
       return 0
    for k,v in kwargs.items():
        print(k,v)

def generate_report( required,/,*,optional="--End of report--"):
    """Generates a report about calculation"""
    #print(required)
    #print(optional)
    return required + optional
    

def main():

 VAT=3 #3%
 unit_price=10 #$
 vat_amount=calculate_vat_amount(unit_price,tax_rate=calculate_tax_rate(VAT))
 #vat_amount=calculate_vat_amount(unit_price,tax_rate=1)
 #vat_amount=calculate_vat_amount(unit_price,tax_rate=0)
 #vat_amount=calculate_vat_amount(0,tax_rate=0)
 print(f"VAT amount---{vat_amount}")

 #price_with_tax=calculate_price_with_tax(12,vat_amount)
 price_with_tax=calculate_price_with_tax(unit_price,vat_amount)
 if not price_with_tax:
    print("ERROR! Please, try calculations again!!!")
 else:
    round_price_with_tax=price_with_tax.quantize(Decimal("1.00")) #view
    print(f"Price with tax: {round_price_with_tax}")

 #TODO add price_with_tax to lst_values, change lst_values(according to user's input)
 lst_keys=["product_ID","product_name","qty","unit_price","price_with_tax"]  #product_ID--int,  qty(int or float), price decimal
 lst_values_1=[1,"Apple",10,12,12.36 ]
 lst_values_2=[2,"Potato",20,13,13.36]
 lst_values_3=[3,"Banana",15,15,15.36]
 product_1=createdict(lst_keys,lst_values_1)
 product_2=createdict(lst_keys,lst_values_2)
 product_3=createdict(lst_keys,lst_values_3)
 print("\n")
 print("----------------PRODUCTS-------------")
 print(product_1)
 print(product_2)
 print(product_3)
 #TODO create database( ID int - value=product{})


 shopping_cart=add(product_1,product_2)
 print("\n")
 print("------------Shopping list---------------")
 print(f"----> In your shopping_cart:\n")
 for i in shopping_cart:
     print(f"{i}\n ")

 total_price_shopping=calculate_total_price_shopping_cart(shopping_cart)
 print(f"Total price of products in shopping cart: {total_price_shopping} USD")
 print("\n")
 print("Unpacking---")
 unpack_product_info(product_ID=1, product_name ='Apple', qty =10, unit_price = 12, price_with_tax = 12.36)
 print("\n")
 
 #generate_report(f"Price calculations were made on the basis of VAT={VAT}")
 rep=generate_report(f"Price calcuations were made on the basis of VAT-{VAT}. ", optional= "The products were fresh and well packaged.")
 print(rep)


if __name__ == "__main__":
    main()