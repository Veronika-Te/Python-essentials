"""Taking natural positive integer"""
def get_positive_integer():
    while(True):
        try:
            input_n=int(input("Please enter natural number: "))
            if input_n>0:
               return input_n
        except:
            print("Please enter integer positive number")

"""Taking input array from user"""
def get_input_list():
   while(True):
       try:
           lst = []
           str_res = input("Enter integer values for array(separated by space): ") 
           res=str_res.split(' ')
           for i in res:
               if i.isnumeric:
                  lst.append(int(i))
           return lst  
       except:
           print("Please enter integer positive number")

"""Taking input string from user"""
def get_input_string():
    while(True):
        try:
            input_str=input("Please enter sentence in order to find first uppercase letter: ")
            input_str=input_str.replace(" ","")
            return(input_str)
        except:
            print("Please enter the sentence")

#1
"""This function prints 0-N(input number) natural numbers"""
def print_natural_numbers(n):
    print("Natural numbers(0-N): \n")
    for i in range(n+1):
        print(i, end = " ")
    print(end="\n")

#2
"""This function prints N(input number)-0 natural numbers"""
def print_reversed_natural_numbers(n):
    print("Natural numbers(N-0): \n")
    for num in range(n, -1, -1) : 
        print(num, end = " ")
    print(end="\n")


#3
"""This function returns elements of the given list"""
def print_elements(input_ls):
   res=""
   for i in input_ls:
       res=res + " " + str(i)
   return res

#4
"""This function return sum of digits of the given number"""
def find_sum_of_digits(input_number):
    s=str(input_number)
    sum_d=0
    for i in s:
        sum_d=sum_d+int(i)
    return sum_d
    
        
#5
"""This function returns first uppercase letter"""
def find_first_uppercase(input_str):
    msg="There are no capitalized letter in the text"
    for char in input_str:
        if char.isupper():
           return char
    return msg

#6
"""This fucntion return minimum value of the given list"""
def find_min_of_list(input_ls):
    return min(input_ls)

def actions_natural_numbers():
    #1,2
    n=get_positive_integer()
    print_natural_numbers(n)
    print("-------------------------------------------")
    print_reversed_natural_numbers(n)
    

def actions_with_digits():
    #4
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
 print("Sum of digits")
 actions_with_digits()
 #5
 actions_with_string()

if __name__=="__main__":
    main()















