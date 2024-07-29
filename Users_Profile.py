def print_message_to_user(name, surname, msg = " "):
    """Greets a user with their full name and a custom message."""
    if not name or surname:
        return " "
    hello=f"Hello {name} {surname}! "
    msg=hello + " " + msg
    return msg

def create_user_profile(name, surname,/, *,age=0, city=" "):
    """Creates a user profile."""
    if not name or not surname:
        return 0
    user_profile_keys=["name", "surname", "age","city"]
    user_profile_values=[]
    user_profile_values.append(name)
    user_profile_values.append(surname)
    user_profile_values.append(age)
    user_profile_values.append(city)
    user_profile=createdict(user_profile_keys, user_profile_values)
    #user_profile=f"Name: {name},\n Surname: {surname}. \n Age: {age}. \n City: {city}"
    return user_profile

def createdict(lst_keys,lst_values):
   """Creates a dictionary for product"""
   if not lst_keys or not lst_values:
       return 0
   return dict(zip(lst_keys,lst_values))

def change_user_settings(user_profile,*,key=" ", value=" "):
    """Changes information about the user"""
    if not user_profile:
        return 0
    user_profile[key]=value
    return user_profile

def change_user_settings_kwargs(**kwargs):
    """Changes information about the user"""
    if not kwargs:
        return 0 
    updated=choose_settings_to_change(kwargs,key="surname", value="Smith")
    return updated

def choose_settings_to_change(dict,*,key=" ", value=" "):
    """Changes dictionary according to the given key and value"""
    if not dict:
        return None
    dict[key]=value
    return dict

def main()->None:

  name="Mary"
  surname="Johanson"
  msg="Welcome to the Python programming world. "
  age=37
  city="New York"


  greet=print_message_to_user(name, surname, msg)
  user_profile=create_user_profile(name, surname, age=37, city="New York")
  print(greet,end='\n')
  print("---USER PROFILE---")
  for key,value in user_profile.items():
      print(key,value)
  print("\n")

  updated_user_profile=change_user_settings(user_profile, key="name", value="Jacob")
  print("---UPDATED---")
  for key,value in updated_user_profile.items():
      print(key,value)
  print("\n")
  print("---UPDATED (with kwargs)---")
  updated=change_user_settings_kwargs(name="Mike", surname="Pitt", age=30, city="London")
  for key,value in updated.items():
      print(key,value)
  print("\n")


if __name__=='__main__':
  main()