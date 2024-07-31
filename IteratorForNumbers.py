def iterate_iterator(iterable)->None:
    """Gets iterator, and iterates(prints) throw elements till the last element"""
    if not iterable:
       return
    
    it=iter(iterable)
    print(it)                   #<list_iterator object at 0x0000023E94773730
    # for i in it: 
    #     print(i)              #prints all elements
    
    while (True):
        try:
            print(next(it))
        except StopIteration:
            print("End of Iteration") 
            return

 
def main()->None:
     iterable=[1,2,3,4,5,6,7,8,9,20]
     #iterable=(10,11,12,13,14,15)
     #iterable="hello"
     #iterable={'1': 'a', '2': 'b', '3':'c'}
     #iterable=([1,2,3,4,5,6,7,8,9,20],[1,2,3])
     iterate_iterator(iterable)
     
if __name__=="__main__":
 main()