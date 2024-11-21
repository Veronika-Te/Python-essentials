import ctypes
from typing import TypeVar
DynamicArray=TypeVar("DynamicArray", bound="DynamicArray")
 
class DynamicArray():
    
    def __init__(self,value:int=10)-> None:
        self.n = 0 # Count actual elements (Default is 0) 
        self.setCapacity(value) # Default Capacity
        self.arr1 = self._make_array(self.getCapacity()) #Array which stores elements
        self._is_hashed = False  # Track if the object has been hashed
        
    def getCapacity(self):
        return self.__capacity
    def setCapacity(self, value=10):
        if value>0:
           if isinstance(value,int):
               self.__capacity=value
           else:
            raise TypeError("Not valid capacity")
        else:
            raise ValueError("Not valid capacity")
    
    def _resize(self, new_capacity:int):
        """ Resizes internal array to new capacity (bigger array), references all existing values """
        arr2 = self._make_array(new_capacity)  
 
        for i in range(self.n):  
            arr2[i] = self.arr1[i]
 
        self.arr1 =  arr2 # Call A the new bigger array
        self.setCapacity(new_capacity)  # Reset the capacity  
    
    def _make_array(self, new_capacity:int): 
        """Method for internal use. Creates a low-level array"""
        if new_capacity<0:
           raise ValueError("Not valid capacity")
        if isinstance(new_capacity,int):
           return (new_capacity * ctypes.py_object)() 
        else: 
           raise TypeError("Not valid capacity")
        
    def __getitem__(self, index: int):
        """ Checks if an array index exists and retrieves the exist element"""
        if not 0 <= index < self.n:
            raise IndexError('Index out of range')
        if not isinstance(index,int):
            raise ValueError("Not valid index")
        return self.arr1[index]   
    
    def __setitem__(self, index:int, value)->None:
        """Sets value at the given index of array"""
        if not 0 <= index < self.n:
            raise IndexError('Index out of bounds!')
        # if self.n == self.capacity:
        #     # Resize the array
        #     self._resize(2 * self.capacity)
        self.arr1[index] = value

    def __len__(self)->int:
        """Returns length of array"""
        if not self.n:
           raise ValueError("Empty array")
        return self.n
    
    def append(self, element):
        """ Appends element to the of the list and resizes the capacity if it is needed"""
        if self.n == self.getCapacity():
            # Resize the array
            self._resize(2 * self.getCapacity())
        self.arr1[self.n] = element #[length]
        self.n += 1 #size + 1
        
    def __iter__(self):
        """Returns an iterator for the dynamic array."""
        for i in range(self.n):
            yield self.arr1[i]
            
    def __repr__(self)->str:
        """Returns a string representation suitable for debugging"""
        if not self.arr1:
            return "Empty Array"
        return f"{self.__class__.__name__}{[x for x in self]!r}".format(self)
        
        
    def __str__(self)->str:
        """Returns a user-friendly string representation"""
        if not self.arr1:
            return "Empty Array"
        return f"{[x for x in self]}"
    
    def __eq__(self, other)->bool:
        """Checks if they are equal"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
            return False  
        if len(self) == len(other):
           for i in range(self.n):
               if self.arr1[i] == other.arr1[i]:
                  return True
               return False 
        return False
    
    def __ne__(self, other)->bool:
        """Checks if they are equal"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
            return True  
        if len(self) != len(other):
           return True
        else:
           for i in range(self.n):
               if self.arr1[i] != other.arr1[i]:
                  return True
               return False 
    
    def __lt__(self,other: DynamicArray)->bool:
        """Checks if elements of array are less than elements of another array"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
           raise TypeError("Wrong type to compare") 
        else:
            for i in range(self.n):
                if self.arr1[i]<other.arr1[i]:
                   return True
                return False 
            
    def __le__(self,other: DynamicArray)->bool:
        """Checks if elements of array are greater than or equal to elements of another array"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
           raise TypeError("Wrong type to compare") 
        else:
            for i in range(self.n):
                if self.arr1[i]<=other.arr1[i]:
                   return True
                return False 
         
            
    def __gt__(self,other: DynamicArray)->bool:
        """Checks if elements of array are greater than elements of another array"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
           raise TypeError("Wrong type to compare") 
        else:
            for i in range(self.n):
                if self.arr1[i]>other.arr1[i]:
                   return True
                return False 
    
    def __ge__(self,other: DynamicArray)->bool:
        """Checks if elements of array are greater than or equal to elements of another array"""
        if not self.arr1 or not other:
           raise ValueError("There is no element to compare") 
        if not isinstance(other, DynamicArray):
           raise TypeError("Wrong type to compare") 
        else:
            for i in range(self.n):
                if self.arr1[i]>=other.arr1[i]:
                   return True
                return False 
         
    def __add__(self,other)->DynamicArray:
        """Concatenate two arrays"""
        if not isinstance(other, DynamicArray):
            raise TypeError("Can only add another DynamicArray.")

        # Create a new DynamicArray to hold the result
        result = DynamicArray()
        
        # Add elements from the first array (self)
        for i in range(self.n):
            result.append(self.arr1[i])
        
        # Add elements from the second array (other)
        for i in range(other.n):
            result.append(other.arr1[i])
        return result
    

    def __iadd__(self,other)->DynamicArray:
        """In place addition"""
        if not isinstance(other, DynamicArray):
            raise TypeError("Can only add another DynamicArray.")
        
        # Add elements from the first array (self)
        for i in range(other.n):
            self.append(other.arr1[i])
        return self
        
        
    #Hashing
    def __hash__(self)->int:
        """Returns Hash code"""
        if not self.arr1:
           return 0
           #raise ValueError("Empty array")
        if not self._is_hashed:
            # Once hashed, prevent further changes
            self._is_hashed = True
        #Tuple=immutable
        tup=tuple(self.arr1[i] for i in range(self.n))
        return hash(tup)
 
def print_rich_comparison(arr,arr2)->None:
    #EqualityCheck
    print(f"{arr}=={arr2}=> {arr == arr2}")    

    #Not equal
    print(f"Not equal? {arr} != {arr2} => {arr!=arr2}")
    
    #less than
    print(f"Check less than:{str(arr)} < {str(arr2)} => {(arr<arr2)}")
    #less than or equal to
    print(f"Check less than or equal to:{str(arr)} <= {str(arr2)} => {(arr<=arr2)}")
    #greater than
    print(f"Check greater than:{str(arr)} > {str(arr2)} => {(arr>arr2)}")
    #greater than or equal to
    print(f"Check greater than or equal to:{str(arr)} >= {str(arr2)} => {(arr>=arr2)}")

def main()->None:
    
    arr = DynamicArray()
    arr2= DynamicArray()
    
    print("Initial capacity:", arr.getCapacity())
    
    arr.append(3)
    arr.append(4)
    
    print("-------Iteration-------")
    #iterate
    for item in arr:
        print(item)
    
    print("-------String representation-------")
        
    print(f"string : {str(arr)}")
    print(f"repr : {repr(arr)}")
    
    arr2.append(2)
    arr2.append(4)
    
    arr3=DynamicArray()
    arr3.append("hello")
    arr3.append("world")
    #Set item
    print("\n-------Set item-------")
    print(f"Before : {arr2}")
    print(f"After setting item: {arr2}")
    print(f"Before: {arr3}")
    v1=5
    v2="everyone"
    arr2[1]=v1
    arr3[1]=v2
    print(f"After setting item: {arr3}")
    
   
    
    #Length
    print(f"\nLength : {len(arr)}")
    
    print("\n-------Rich comparisons-------")
    #Rich comparisons
    print_rich_comparison(arr,arr2)
    
    #Add
    print("\n-------Adding result-------")
    res=arr+arr2
    print(res)
    
    #+=
    print("-------In place addition-------")
    arr += arr2
    print(str(arr))
    print("-------Hashing-------")   
    #Hash
    print(f"\nHash code: {hash(arr)}")    
    
       
if __name__ == "__main__":
     main()
    
