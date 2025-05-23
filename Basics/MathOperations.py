import math

def square(num)->int:
    """Calculates square of the given number"""
    if not num:
       return 0 
    return num**2

def cube(num)->int:
    """Calculates cube of the given number"""
    if not num:
       return 0 
    return num**3

def square_root(num)->float:
    """Calculates square root of the given number"""
    if not num:
       return 0 
    return num**(1/2) 

def factorial(num)->int:
    """Calculates factorial of the given number"""
    if not num:
       return 0  
    fact = 1
    for i in range(1, num+1):
        fact = fact * i 
    return fact


def get_keys(dictionary):
    """Creates set with keys of the given dictionary"""
    if not dictionary: 
       return
    return set(dictionary.keys())

def math_operations(number, operation):
    """Uses this dictionary to apply the requested math function to a number."""
    math_operations_dict={ 'Square':square, 'Cube':cube , 'Square root':square_root, 'Factorial':factorial}
    if not number or not operation:
       return 0
    
    #set of keys
    keys=get_keys(math_operations_dict)

    if operation in keys:
        if operation=='Square':
            sq=math_operations_dict.get(operation)
            res=sq(number)
            return res
        elif operation=='Cube':
            cb=math_operations_dict.get(operation)
            res=cb(number)
            return res
        elif operation=='Square root':
            sr=math_operations_dict.get(operation)
            res=sr(number)
            return res
        elif operation=='Factorial':
            fc=math_operations_dict.get(operation)
            res=fc(number)
            return res

        else:
            return 0
        
    else:
        return 0
    

def main():
   
   print("Math operations")
   number=int(input("Please enter integer number: "))
   #number=5
   print("\n")
   
   print('Square')
   sq=math_operations(number, 'Square')
   print(sq)
   print("\n")

   print('Cube')
   cb=math_operations(number, 'Cube')
   print(cb)
   print("\n")

   print('Square root')
   sr=math_operations(number, 'Square root')
   print(sr)
   print("\n")

   print('Factorial')
   fc=math_operations(number, 'Factorial')
   print(fc)
   print("\n")
   
if __name__=="__main__":
    main()
