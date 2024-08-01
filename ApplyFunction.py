def powerOfTwo(number:int)->int:
    """Gets the number,and returns number's power of two"""
    if not number:
       return 0
    number=number**2
    return number

def apply_function(iterable, func:callable)->list:
    """Applies the function to each element of the iterable, returning a list of the results."""
    if not iterable or not func:
        return []
    it=iter(iterable)
    result=[]
    for i in it:
        result.append(func(i))
    return result

if __name__=="__main__":   
 numbers=[1,2,34,4,5]
 res=apply_function(numbers, powerOfTwo)
 print(res)