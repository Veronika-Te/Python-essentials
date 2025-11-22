from typing import List

def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of a target element.

    Parameters:
    arr (list): A sorted list of comparable elements.
    target: The element to search for in the array.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
      
    if len(arr) == 0:
      raise ValueError("arr must not be empty")

    if not isinstance(target, (int, float)):
      raise TypeError("All elements in arr must be numbers")

    for item in arr:
        if type(item) != type(target):
          raise TypeError("All elements in arr must be of the same type as target")
    # Ensure the array is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
      raise ValueError("arr must be sorted for binary search")
   
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  
        if guess > target:
            high = mid - 1  
        else:
            low = mid + 1   
    return -1

if __name__ == "__main__":
  
  #sorted array
  my_list = [1, 3, 5, 7, 9, 11, 13, 15] 
  target = 7

  index = binary_search(my_list, target)
  
  print(f"Element '{target}' found at index: {index}" if index !=-1 else f"Element '{target}' not found")