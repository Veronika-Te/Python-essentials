def get_positive_integer():
    """Taking natural positive integer"""
    while(True):
        try:
            input_n=int(input("Please enter natural number: "))
            if input_n>0:
               return input_n
        except:
            print("Please enter integer positive number")

def get_input_list():
   """Taking input array from user"""
   while(True):
       try:
           lst = []
           print("\n")
           str_res = input("Enter integer values for array(separated by space): ") 
           res=str_res.split(' ')
           for i in res:
               if i.isnumeric:
                  lst.append(int(i))
           return lst  
       except:
           print("Please enter correct values for array(positive integers)")


def get_input_string():
    """Taking input string from user"""
    while(True):
        try:
            input_str=input("Please enter sentence in order to find first uppercase letter: ")
            input_str=input_str.replace(" ","")
            return(input_str)
        except:
            print("Please enter the sentence")

#1
def print_natural_numbers(n):
    """This function prints 0-N(input number) natural numbers"""
    print("Natural numbers(0-N): \n")
    if not n:
        return
    for i in range(n+1):
        print(i, end = " ")
    print(end="\n")

#2
def print_reversed_natural_numbers(n):
    """This function prints N(input number)-0 natural numbers"""
    print("Natural numbers(N-0): \n")
    if not n:
        return
    for num in range(n, -1, -1) : 
        print(num, end = " ")
    print(end="\n")


#3
def print_elements(input_ls):
   """Returns elements of the given list"""
   if not input_ls:
       return " "
   res=""
   for i in input_ls:
       res=res + " " + str(i)
   return res

#4
def find_sum_of_digits(input_number):
    """Returns sum of digits of the given number"""
    if not input_number:
        return
    s=str(input_number)
    sum_d=0
    for i in s:
        sum_d=sum_d+int(i)
    return sum_d
    
        
#5
def find_first_uppercase(input_str):
    """Returns first uppercase letter"""
    if not input_str:
        return " "
    msg="There are no capitalized letter in the text"
    for char in input_str:
        if char.isupper():
           return char
    return msg

#6
def find_min_of_list(input_ls):
    """Returns minimum value of the given list"""
    if not input_ls:
        return 
    return min(input_ls)

def actions_natural_numbers():
    #1,2
    n=get_positive_integer()
    print_natural_numbers(n)
    print("-------------------------------------------")
    print_reversed_natural_numbers(n)
    

def actions_with_digits():
    #4
    print("For calculating sum of digits \n")
    input_number=get_positive_integer()
    res=find_sum_of_digits(input_number)
    if res:
       print(f"Sum of digits {res}")
    else:
       print("Please enter integer")
    
 
def actions_with_list():
     input_ls=get_input_list()
     res=print_elements(input_ls)
     res2=find_min_of_list(input_ls)
     if res:
        print(f"Elements of the initial list: {res}")
    #6
     if res2:
        print(f"Min value in the intial list is {res2}")
     else:
        print("The list is empty")
     

def actions_with_string():
    #5
    input_str=get_input_string()
    res=find_first_uppercase(input_str)
    if res:
       print(f"Result: {res}")
    else:
       print("The string is empty")
    
       

def main():
 #1,2
 actions_natural_numbers()
 #3,6
 actions_with_list()
 #4
 print("-----")
 print("\n")
 print("____Sum of digits___")
 actions_with_digits()
 #5
 actions_with_string()

if __name__=="__main__":
    main()

    