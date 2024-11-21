from typing import Iterable
def powerOfTwo(*numbers:int)->int:
    """Gets the number,and returns number's power of two"""
    if not numbers:
       return 0
    res=[] 
    for i in numbers: 
        for j in i:
            j=j**2
            res.append(j)
    return res

def apply_function(*iterable: Iterable, func:callable)->list:
    """Applies the function to each element of the iterable, returning a list of the results."""
    if not iterable or not func:
        return []
    it=iter(iterable)
    result=[]
    for i in it:
        result.append(func(*i))
    return result

def main()->None:
    numbers=([1,2,34,4,5],[1,2,3])
    res=apply_function(numbers, func=powerOfTwo)
    print(res)
    
if __name__=="__main__":   
    main()
 