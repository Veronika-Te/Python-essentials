"""This function validates input username"""
def is_username_validated(input_username):
    if not input_username:
       print("Please enter Username!!")
       return False

    input_username=input_username.replace(" ", "")
    reserved_words={"admin","root","False", "True", "None","if","return","while","try","finally","continue"}
    length_username =len(input_username)
    
    if length_username<5:
        print("The lenght is too short, should be more than 5 characters")
        return False
    elif length_username>20:
        print("The lenght is too long, should be less than 20 characters")
        return False
    elif not input_username.isalnum():
        print("Please enter alphanumeric characters [A-Z],[a-z],[0-9]")
        return False
    elif input_username in reserved_words:
            print("!!! Enter valid username which contains your name")
    else:
            return True

#TODO if inputusername in dictofusers search , in order to be unique
#       try again


"""This function validates phonenumber"""
def  is_phonenumber_validated(phonenumber):
    if not phonenumber:
       print("Please Enter phone number")
       return False
    
    phonenumber=phonenumber.replace(" ", "")
    #print(phonenumber)
    print(type(phonenumber))
    length_phnum=len(phonenumber)
    if (phonenumber[0] == "0") & (length_phnum==9): #count of digits in phone numbers (in Armenia) started with number "0"
        if int(phonenumber[1:9]):
           return True     
        else:
           return False
    elif (phonenumber[0]=="+") & (phonenumber[1:4]=="374") & (length_phnum==12):
         if int(phonenumber[1:12]): 
            return True
         else:
            return False
    else: 
         print("Please enter valid phone number")
         return False

"""This function validates email"""
def is_email_validated(input_email):
    if not input_email:
       print("Please enter valid Email address")
       return
    at_symbol_i=input_email.find("@")
    dot_symbol_i=input_email.find(".") 
    input_email=input_email.replace(" ","")
    if dot_symbol_i>at_symbol_i:
       flag1=False            
       flag2=False
       flag3=False  

       substring1=input_email[0:at_symbol_i]
       if len(substring1)<=3:
          print("Email address is too short")
          flag1=False
       elif len(substring1)>=20:
          print("Email address is too long")
          flag1=False
       else:
          flag1=True
       
        
       substring2=input_email[at_symbol_i:(dot_symbol_i + 1)]
       if len(substring2)<=3:
          flag2=False
       elif len(substring2)>=10:
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

       return flag1 & flag2 & flag3

    else:
        return False


"""This function validates password"""
def is_password_validated(input_password):
    if(len(input_password)>=8):
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
        print("The lenght is too short, should be at least 8")

    return flag1 & flag2 & flag3 & flag4

    

if __name__ == '__main__':
    #USERNAME
    while(True):
        try:
            input_username=input("Please enter Username:")
            if is_username_validated(input_username):
               print("Validated username:", input_username)
               break
            else:
               print("Not validated, please try again")
               
        except:
            print("Please enter valid username")
           
    #PHONENUMBER
    while(True):
        try:
            input_phonenumber=input("Please enter your phone number: ")
            if is_phonenumber_validated(input_phonenumber):
               print("Validated phone number:",input_phonenumber)
               break
            else:
               print("Enter valid phone number in Armenia +374XXXXXX or 0XXXXXXXX")
        except:
            print("Enter valid phone number in Armenia +374XXXXXX or 0XXXXXXXX")

    
    #EMAIL
    while(True):
        try: 
            input_email=input("Please enter your email: ")
            if is_email_validated(input_email):
               print("Validated Email address:",input_email)
               break
            else:
               print("Enter valid Email address")
        except:
            print("Enter valid Email address")

    #PASSWORD
    repeat=2
    while(True):
        try: 
            input_password=input("Please enter password: ")
            if is_password_validated(input_password):
               print("Validated Password:",input_password)
               repeat_password=input("Please reenter your password: ")
               #repeat validation
               if(repeat_password==input_password):
                   print("Congratulations, you are registered")
                   break
               else:
                   print("Please try again")
                   continue    
            else:
               print("Enter valid Password")
        except:
            print("Enter valid Email address")

     

    ls=[]
    ls.append(input_username)
    ls.append(input_phonenumber)
    ls.append(input_email)
    ls.append(input_password)
    print(ls)


    
    


