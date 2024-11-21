def get_nth_element(iterable, number: int):
    """Takes an iterable and an integer n, and returns the n-th element from the iterable using iter() and next()."""
    if not iterable or not number:
       return 
    it=iter(iterable)
    i=0
    while(True):
        try:
            i+=1
            if number==i:
               print(f"Position: {number} ")
               return (next(it))
            else:
               next(it)
        except:
            print("End")
            break

if __name__=="__main__":           
        
 numbers=[1,2,3,4,89,511,655,7,78]
 index=6
 res=get_nth_element(numbers, index)
 print(f"Value: {res}")
