#Closures
def make_multiplier_of(n:int)->callable:
    """ Takes an integer n and returns a function that multiplies its argument by n"""
    def multiply():
        print(n * n)
    return multiply


def make_counter(counter: int =0)->callable:
    """Returns a function that, when called, increments and returns a counter variable. 
    The counter starts at 0 and increments by 1 each time the function is called."""
    def increment_counter():
        nonlocal counter
        counter+=1
        print(counter)
    return increment_counter

def main()->None:
   
   print("_____ Multiplier")
   res=make_multiplier_of(7)
   res()
   res2=make_multiplier_of(8)
   res2() 
   print("_____Counter")
   res3=make_counter(0)    
   res3()

if __name__=="__main__":
 main()