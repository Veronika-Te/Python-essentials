def sum(*args)-> int:
    """Finds sum of the given list"""
    if not args:
        return 0
    sum=0
    for i in args:
        for j in i:
            sum+=j
    return sum

def find_max(*args)-> int: 
    """Finds max of the given list"""
    if not args:
        return 0
    for i in args:
        my_max=i[0]
        for j in i:
            if j>my_max:
               my_max=j
        return my_max

def find_min(*args)-> int: 
    """Finds max of the given list"""
    if not args:
        return 0
    for i in args:
        my_min=i[0]
        for j in i:
            if j<my_min:
               my_min=j
        return my_min

def process_data(data: list,/,*,operation):
    """Processes data with different operations."""
    if not data or not operation:
        return 0
    return operation(data)

def main()->None:
   ls=[1,2,3,4,5,6,7]
   res=process_data(ls,operation=sum)
   print(f"Sum of elements: {res}")
   max_of_ls=process_data(ls,operation=find_max)
   print(f"Max of elements: {max_of_ls}")
   min_of_ls=process_data(ls,operation=find_min)
   print(f"Min of elements: {min_of_ls}")

if __name__=="__main__":
   main()
