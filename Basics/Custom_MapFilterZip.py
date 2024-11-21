#_________________Map____________________

def add_2(*iterables):
    if not iterables:
        return []
    n=2
    res=[]
    for i in iterables:
        for j in i:
            res.append(j+2)
    return res     

def custom_map(operation: callable, *iterables)->list:
    """Represents map function.Iterates over each element in the iterable 
    and applies operation to the elements, appends to list and returns"""
    if not iterables or not operation:
        return []
    result=[]
    for items in zip(*iterables): #iterables=([1, 2, 3], [3, 4, 7]), 1 cycle items=(1,3) 2) (2,4) 3) (3,7)
        res=operation(items)
        result.append(res)
    return result

#_________________Filter____________________

def isEven(n:int)->bool:
    if not n:
        return 0
    return n%2==0

def custom_filter(operation: callable, iterables)->list:
    """Represents filter function. Iterates over each element in the iterable and applies to each element function(result is boolean value). 
    If for specific item this function returns True value, then those items are being collected in the result list """ 
    if not operation or not iterables:
        return []
    result=[]
    for item in iterables:
        if operation(item):
           result.append(item)
    return result

#_________________Zip____________________

def custom_zip(*iterables, strict=False) ->list: #iterables=tuple
    """Represents zip function. Iterates over each element in the iterables, calculates the minimum length of list( in iterables). By iterating in the size of minimum length,
    creating couples of elements based on their positions in the lists(in iterables), then these couples appends to list, which casts into tuple type and returned"""
    if not iterables:
       return []
    # min_length=len(iterables[0])
    # for i in range(1,len(iterables)):
    #     if min_length>len(iterables[i]):  
    #        min_length=len(iterables[i])
    # print(iterables[0])

    #using built in min function
    min_length = min(len(it) for it in iterables)
    res = [tuple([item[i] for item in iterables]) for i in range(min_length)]
    
    # res=[]
    # for i in range(min_length):
    #     tmp=[]
    #     for item in iterables:
    #         tmp.append(item[i])
    #     res.append(tuple(tmp)) 
    return res




def main():
   
   #one item to map
   print("___Custom Map___\n") 
   numbers2 = [4, 5, 6]
   res=custom_map(add_2, numbers2)
   for i in res:
       print(i)

   print("\n")
   #Multiple adds map
   print("___Custom Map___")
   print("with 2 arguments\n")

   numbers1 = [1, 2, 3]
   numbers2 = [4, 5, 6]
   res=custom_map(add_2, numbers1,numbers2)
   for i in res:
       print(i)
   print("\n")
       
   #Custom Filter
   print("___Custom Filter___\n") 
   #lst=[1,2,3,3]
   tpl=(1,2,2,3)
   result=custom_filter(isEven, tpl)
   print(result)
   print("\n")
   
   #Custom Zip
   print("___Custom Zip___\n") 
   names=["James","Bob","Ann"]
   ages=[23,34,16,17]
   res=custom_zip(names,ages)
   for i in res:
       print(i)
   print("\n")

    

if __name__== "__main__":
    main()
  
  