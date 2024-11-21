def uppercase(input_str)->str:
    """Converts a string to upper case letters."""
    if not input_str:
       return " "
    input_str=input_str.upper()
    return input_str

def lowercase(input_str)->str:
    """Converts a string to lower case letters."""
    if not input_str:
       return " "
    input_str=input_str.lower()
    return input_str

def title(input_str)->str:
    """Converts the first character of the string to a capital """
    if not input_str:
       return " "
    input_str=input_str.capitalize()
    return input_str

def reverse(input_str)->str:  
    """Reverses string"""
    if not input_str:
       return " "
    input_str=input_str[::-1]
    return input_str

def manipulate_string(s:str, operation:callable)->str:
    """Takes a string and an operation name, 
    and uses the dictionary to perform the requested string manipulation."""
    str_manipulations={'U': uppercase,'L': lowercase, 'T': title, 'R' : reverse}
    if not s or not operation:
       return " "
    if operation==uppercase:
       operation=str_manipulations.get('U')
       return operation(s)
    elif operation==lowercase:
       operation=str_manipulations.get('L')
       return operation(s)
    elif operation==title:
       operation=str_manipulations.get('T')
       return operation(s)
    elif operation==reverse:
       operation=str_manipulations.get('R')
       return operation(s)
    else:
        return " "

def get_input()->str:
    """Gets input from user"""
    #TODO add action input
    while True:
        try:
            input_str=input("Please enter the word you want to change(length>4)): ")
            input_str=input_str.replace(" ", "")
            if not input_str:
               return "There is no input"
            if len(input_str)>4:
               if input_str.isalpha():
                   return input_str
        except:
            print("Enter valid word")

def main()->None: 
    
    input_str=get_input()
    print("String Manipulations")
    print("___Reverse___")
    print(manipulate_string(input_str,reverse))
    print("\n")
    print("___Uppercase___")
    print(manipulate_string(input_str,uppercase))
    print("\n")
    print("___Lowercase___")
    print(manipulate_string(input_str,lowercase))
    print("\n")
    print("___Title___")
    print(manipulate_string(input_str,title))
    print("\n")

if __name__=="__main__":
     main()

