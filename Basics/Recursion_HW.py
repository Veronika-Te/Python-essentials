
def print_numbers_recursive(n):
    """Recursive function. Prints numbers from 1 to 5."""
    if n==0:
       return " "
    print_numbers_recursive(n-1)
    print(n)
    return " "

def print_numbers_recursive_reversed(n):
    """Recursive function. Prints numbers from 5 to 1."""
    if n==0:
       return " "
    print(n)
    print_numbers_recursive_reversed(n-1)
    return " "


def factorial_recursive(n):
    """Recursive function. Calculates the factorial of a given number."""
    if n<=1:
        return 1
    return n * factorial_recursive(n-1) 

def acc_recursive(n):
    """Recursive function. Finds the sum of the first N natural numbers."""
    if n<2:
       return 1
    return n + acc_recursive(n-1)


def isPalindrome_recursive(input_str):
    """Recursive function. Checks if a given string is a palindrome."""
    if len(input_str) <= 1:
        return True
    else:
        return input_str[0] == input_str[-1] and isPalindrome_recursive(input_str[1:-1])

def reverse_recursive_2(s):
    """Recursive function. Reverses a given string. Classwork version"""
    if not s:
       return " "
    else:
       return reverse_recursive_2(s[1:]) + s[0]

def fibonacci_recursive(n):
   """Recursive function. Generates the Nth Fibonacci number."""
   if n <=1:
       return n
   else:
       return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))


def print_list_recursive( lst , index=0):
    """Recursive function. Prints all elements of a list."""
    if not lst:
        return " "
    if (index>=0):
        print_list_recursive(lst,index-1)
        print (str(lst[index]) + " at index " + str(index))
    

def count_elements_recursion(lst):
    """Recursive function. Finds the length of a list."""
    if not lst:
        return 0
    return 1 + count_elements_recursion(lst[1:])

def findSum(lst, length):
    """Recursive function. Finds sum of array elements using recursion"""
    if length<=0:
        return 0
    else:
        return findSum(lst, length-1) + lst[length-1]

def isSorted(lst):
    """Recursive function to check if a list is sorted in ascending order"""
    if len(lst) in [0,1]:
        return True
    if lst[0]<=lst[1]:
        return isSorted(lst[1:])
    return False

def main()->None:
    #TODO add user input
    n=5
    # 1 2 3 4 5...n
    print("Numbers recursive: ")
    res=print_numbers_recursive(n)
    print(res) 

    print("\n") 
    # n...5 4 3 2 1
    print("Numbers(reversed) recursive: ")
    res2=print_numbers_recursive_reversed(n)
    print(res2) 

    #Factorial
    f=factorial_recursive(n)
    print(f"Factorial: {n}! = {f} ")

    #Sum of the first N natural numbers
    print("\n")  
    res=acc_recursive(5)
    print(f"Sum of the first N natural numbers: { res}")
    print("\n") 

    #Reverses string
    s="Hello"
    z=reverse_recursive_2(s)
    print("Reversed string:", z)
    print("\n")
 
    #Fibonacci
    n=10
    if n <= 0:
       print("Plese enter a positive integer")
    else:
       print("Fibonacci sequence:")
    for i in range(n+1):
        print(fibonacci_recursive(i))

    print("\n")

    #Checks if a given string is a palindrome
    s="paramarap"
    res3=isPalindrome_recursive(s)
    print(f"{s} is palindrome? : {res3}")

    #Prints all elements of a list
    lst = [11,22,33,44]
    print_list_recursive(lst, len(lst)-1)
    print("\n")

    #Length of list
    length=count_elements_recursion(lst)
    print(f"Length of list: {length}")

    #Sum of list's elements
    lst=[1,2,3,4,5,8]
    lenght=len(lst)
    sum_lst=findSum(lst, lenght)
    print("Sum of elements in list", sum_lst)

    #If list is sorted
    answer=isSorted(lst)
    if answer:
        print(f"{answer}. The list is in ascending order.")
    else:
        print(f"{answer}. The list is not sorted.")

if __name__=="__main__":
    main()
 



