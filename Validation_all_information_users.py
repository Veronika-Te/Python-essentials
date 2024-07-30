def is_username_validated(input_username):
    """Validates input username"""
    if not input_username:
       print("Please enter Username!!")
       return False

    input_username=input_username.replace(" ", "")
    reserved_words={"admin","root","False", "True", "None","if","return","while","try","finally","continue"}
    length_username =len(input_username)
    
    min_len=5
    max_len=20
    if length_username<min_len:
        print("The lenght is too short, should be more than 5 characters")
        return False
    elif length_username>max_len:
        print("The lenght is too long, should be less than 20 characters")
        return False
    elif not input_username.isalnum():
        print("Please enter alphanumeric characters [A-Z],[a-z],[0-9]")
        return False
    elif input_username in reserved_words:
         print("!!! Enter valid username which contains your name")
         return False
    else:
         return True

#TODO if inputusername in dictofusers search , in order to be unique
#       try again

def  is_phonenumber_validated(phonenumber):
    """Validates phonenumber"""
    if not phonenumber:
       print("Please Enter phone number")
       return False
    
    phonenumber=phonenumber.replace(" ", "")
    #print(phonenumber)
    print(type(phonenumber))
    length_phnum=len(phonenumber)
    defined_len1=9 #count of digits in phone numbers (in Armenia) started with number "0"
    defined_len2=12 #count of digits in phone numbers (in Armenia) started with number "+374"
    if (phonenumber[0] == "0") and (length_phnum==defined_len1): #count of digits in phone numbers (in Armenia) started with number "0"
        if int(phonenumber[1:9]):
           return True     
        else:
           return False
    elif (phonenumber[0]=="+") and (phonenumber[1:4]=="374") and (length_phnum==defined_len2):
         if int(phonenumber[1:12]): 
            return True
         else:
            return False
    else: 
         
         print("Please enter valid phone number")
         return False


def is_email_validated(input_email):
    """Validates email"""
    if not input_email:
       print("Please enter valid Email address")
       return
    at_symbol_i=input_email.find("@")
    dot_symbol_i=input_email.find(".") 
    input_email=input_email.replace(" ","")
    min_len=3
    if dot_symbol_i>at_symbol_i:
       flag1=False            
       flag2=False
       flag3=False  

       substring1=input_email[0:at_symbol_i]
       max_len_sub1=20
       if len(substring1)<=min_len:
          print("Email address is too short")
          flag1=False
       elif len(substring1)>=max_len_sub1:
          print("Email address is too long")
          flag1=False
       else:
          flag1=True
       
       max_len_sub2=10
       substring2=input_email[at_symbol_i:(dot_symbol_i + 1)]
       if len(substring2)<=min_len:
          flag2=False
       elif len(substring2)>=max_len_sub2:
          flag2=False
       else:
          if substring2[1:(len(substring2)-1)].isalpha():
             flag2=True
          else:
             flag2=False
       
       substring3=input_email[dot_symbol_i : (len(input_email))]
       
       if len(substring3)<5: 
           if substring3[1:].isalpha():
              flag3=True
           else:
              flag3=False

       return flag1 and flag2 and flag3

    else:
        return False



def is_password_validated(input_password):
    """Validates password"""
    max_len=8
    if(len(input_password)>=max_len):
       flag1=False
       flag2=False
       flag3=False
       flag4=False
       special_sym ={'!','$', '@', '#', '%','^','&','*'}
       for char in input_password:
           if char.isdigit():
              flag1=True
           elif char.isupper():
              flag2=True    
           elif char.islower():
              flag3=True
           elif char in special_sym:
              flag4=True
           else:
                flag1=False
                flag2=False
                flag3=False
                flag4=False
    else:
        print("The length is too short, should be at least 8")

    return flag1 and flag2 and flag3 and flag4

def get_valid_username():
    """Gets input username and check if info was validated"""
    while(True):
        try:
            input_username=input("Please enter username:")
            if is_username_validated(input_username):
               print("Validated username:", input_username)
               return input_username
            else:
               print("Not validated, please try again")
        except:
            print("Please enter valid username")
           

def get_valid_phonenumber():
    """Gets input phonenumber and check if info was validated"""
    while(True):
        try:
            input_phonenumber=input("Please enter your phone number: ")
            if is_phonenumber_validated(input_phonenumber):
               print("Validated phone number:",input_phonenumber)
               return input_phonenumber
            else:
               print("Enter valid phone number in Armenia +374XXXXXX or 0XXXXXXXX")
        except:
            print("Enter valid phone number in Armenia +374XXXXXX or 0XXXXXXXX")

def get_valid_email():
    """Gets input email and check if info was validated"""
    while(True):
        try: 
            input_email=input("Please enter your email: ")
            if is_email_validated(input_email):
               print("Validated Email address:",input_email)
               return input_email
            else:
               print("Enter valid Email address")
        except:
            print("Enter valid Email address")

def get_valid_password():
    """Gets input password and check if info was validated, if it was validated, then checks match of repeated password"""
    while(True):
        try: 
            input_password=input("Please enter password: ")
            if is_password_validated(input_password):
               print("Validated Password:",input_password)
               repeat_password=input("Please reenter your password: ")
               #repeat validation
               if(repeat_password==input_password):
                   return input_password
               else:
                   print("Please try again")
                   continue    
            else:
               print("Enter valid Password")
        except:
            print("Enter valid Email address")

def collect_info_of_the_user(input_username,input_phonenumber,input_email,input_password):
    """Collects info about one user"""
    ls=[]
    ls.append(input_username)
    ls.append(input_phonenumber)
    ls.append(input_email)
    ls.append(input_password)
    return ls

def main():
    #USERNAME
    username=get_valid_username()
    #PHONENUMBER
    phonenumber=get_valid_phonenumber()
    #EMAIL
    email=get_valid_email()
    #PASSWORD
    password=get_valid_password()

    ls=collect_info_of_the_user(username,phonenumber,email,password)
    print("Congratulations, you are registered")
    for i in ls:
        print(i)

if __name__ == '__main__': 
    main()
  

