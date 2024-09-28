import ctypes
 
 
class DynamicArray():
    
    def __init__(self)-> None:
        #TODO add encapsulation
        self.n = 0 # Count actual elements (Default is 0) #?
        self.capacity = 10 # Default Capacity
        self.arr1 = self._make_array(self.capacity) #Array which stores elements
        self._is_hashed = False  # Track if the object has been hashed
       
    def _resize(self, new_capacity):
        """ Resizes internal array to new capacity (bigger array), references all existing values """
        arr2 = self.make_array(new_capacity)  
 
        for i in range(self.n):  
            arr2[i] = self.arr1[i]
 
        self.arr1 =  arr2 # Call A the new bigger array
        self.capacity = new_capacity  # Reset the capacity  

    def __getitem__(self, index: int):
        """ Checks if an array index exists and retrieves the exist element"""
        if not 0 <= index < self.n:
            raise IndexError('Index out of range')
        if not isinstance(index,int):
            raise ValueError("Not valid index")
        return self.arr1[index]  
    
    def _make_array(self, new_capacity): 
        """Method for internal use. Creates a low-level array"""
        if new_capacity<0:
           raise ValueError("Not valid capacity")
        if isinstance(new_capacity,int):
           return (new_capacity * ctypes.py_object)() 
        else: 
           raise ValueError("Not valid capacity")
    
    def __len__(self)->int:
        """Returns length of array"""
        return self.n
    
    def append(self, element):
        """ Appends element to the of the list and resizes the capacity if it is needed"""
        if self.n == self.capacity:
            # Resize the array
            self._resize(2 * self.capacity)
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
    
    def __eq__(self, other):
        """Checks if they are equal"""
        if not isinstance(other, DynamicArray):
            return False  
        if len(self) == len(other):
           for i in range(self.n):
               if self.arr1[i] == other.arr1[i]:
                  return True
               return False 
        return False
    
    def __hash__(self):
        """Returns Hash code"""
        if not self.arr1:
           raise ValueError("Empty array")
        if not self._is_hashed:
            # Once hashed, prevent further changes
            self._is_hashed = True
        #Tuple=immutable
        tup=tuple(self.arr1[i] for i in range(self.n))
        return hash(tup)
 
       

def main()->None:
    arr = DynamicArray()
    arr2=DynamicArray()
    print("Initial capacity:", arr.capacity)
    arr.append(3)
    arr.append(4)
    #iterate
    for item in arr:
        print(item)
        
    print(f"string : {str(arr)}")
    print(f"repr : {repr(arr)}")
    
    arr2.append(3)
    arr2.append(4)
    
    #EqualityCheck
    if arr==arr2:
       print("True")
    else:
        print("False")
        
    #Hash
    print(hash(arr))    
    
       
if __name__ == "__main__":
     main()
    
