def sorting(lst):
    if not lst:
        return [ ]
    lst.sort()
    return lst
    
def reversing(lst):
    if not lst:
        return [ ]
    return lst[::-1]
    
def filtering(lst):
    if not lst:
        return [ ]
    f=filter(lambda x: x%2!=0, lst)
    return f

def mapping(lst):
    if not lst:
        return [ ]
    m=map(lambda x: x**2 , lst)
    return m


list_transformations={'Sorting':sorting ,'Reversing': reversing,'Filtering': filtering ,'Mapping': mapping}
def  transform_list(lst:list, operation:str)->list:
     #list_transformations={'Sorting':sorting ,'Reversing': reversing,'Filtering': filtering ,'Mapping': mapping}  
     if not lst or not operation:
        return [ ]
    
     lst_actions={'Sorting','Reversing','Filtering','Mapping' }
     if operation in lst_actions:
        if operation == 'Sorting':
           sorting=list_transformations.get(operation)
           return sorting(lst)
        elif operation == 'Reversing':
           reversing=list_transformations.get(operation)
           return reversing(lst)
        elif operation == 'Filtering':
           filtering=list_transformations.get(operation)
           f=filtering(lst) 
           filtered=[]
           for i in f:
               filtered.append(i)
           return filtered
        elif operation == 'Mapping':
           mapping=list_transformations.get(operation)
           m=mapping(lst)
           mapped=[]
           for i in m:
               mapped.append(i)
           return mapped
        else:
            return " "
     else:
         return [ ]

         
def main(): 
   #TODO add user input  

   lst=[1,2,3,4,5,4,5,5,6]
   print("Sorting")
   sorted=transform_list(lst, "Sorting")
   print(sorted)
   print("\n")
   
   print("Reversing")
   reversed=transform_list(lst, "Reversing")
   print(reversed)
   print("\n")


   print("Filtering")
   filtered=transform_list(lst, "Filtering")
   print(filtered)
   print("\n")
   
   print("Mapping")
   mapped=transform_list(lst, "Mapping")
   print(mapped)
   print("\n")

if __name__=="__main__":
    main()
    
