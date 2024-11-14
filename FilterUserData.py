import json

def parse_json(file_path):
    """Parsing JSON"""
    try:
        with open(file_path, "r") as file:
             data=json.load(file)
             return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file '{file_path}'")
    except Exception as e:
        raise ValueError(f"An error occurred while parsing JSON from '{file_path}': {e}")
    
def filtering_json(data:dict, filter_age:int , position:str):
   """Filtering JSON file by the given criterias"""
   if not data or not filter_age or not position:
      raise ValueError("Invalid parameters")
    
   set_of_positions={"Software Engineer", "Manager","Data Analyst","Manager","Graphic Designer","Project Manager"}   
   
   if not isinstance(filter_age,int) or not 0<filter_age<100:
      raise ValueError("Not valid age")
   if not isinstance(position,str) or  not position in set_of_positions :
      raise ValueError("Not valid position")
   
   main_key="users"
   if main_key in data:
      lst_users=data.get(main_key)
      res=[]
      filtered_dict={}
      if not isinstance(lst_users,list):
         raise TypeError("Not valid data for users")
      for dicts in lst_users:
          if dicts.get("age")<=filter_age and dicts.get("position")==position:
             res.append(dicts)
             # dict with users which are matching the given criterias
             filtered_dict[main_key]=res
      return filtered_dict 
   else:
       raise ValueError("Not valid key for data")
              

def validate_file_name(name_json:str="new")->str:
    """Validates the name of the JSON file; the default name is 'new'."""
    if not name_json:
       raise ValueError("Empty name")
    if isinstance(name_json,str):
       if name_json.replace(" ",""):
          if name_json.isascii():
             extension_str=".json"
             name_json=name_json+extension_str
             return name_json
          else:
                raise ValueError("Name should be ASCII") 
       else:
          raise ValueError("Empty name")
    else:
       raise TypeError("Not valid type for the name")
    
def process_to_JSON(raw_json:dict, file_name:str="new")->None:
    """By processing raw data, writes to JSON file"""
    if not raw_json:
       raise ValueError("Empty raw json")
    if not isinstance(raw_json,dict):
       raise TypeError("Not valid type for converting to JSON") 
    
    f_name=validate_file_name(file_name)
    try:
        #using 'x' mode to ensure we create a new file and avoid overwriting
        with open(f_name,"x") as file:
            json.dump(raw_json,file, indent=2)
            print("Succesfully done!")

    except TypeError as e:
        # non-serializable object. 
        raise TypeError(f"JSON encoding error") from e
    except FileExistsError as e:
        raise FileExistsError(f"Error {f_name} already exists") from e
    except Exception as e:
        raise Exception(f" Unexpected error occured") from e
   
           
def main():  
    try:
        file_path="user_data.json"
        data_json=parse_json(file_path)
        filter_age=35
        position="Manager"
        data=filtering_json(data_json, filter_age,position)
        process_to_JSON(data, "filtered_users")
    except Exception as e:
        print(f"{e}")
        
    
if __name__=="__main__":
    main()
