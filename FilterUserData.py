import json

def parse_json(file_path):
    """Parsing JSON"""
    try:
        with open(file_path, "r") as file:
             data=json.load(file)
             return data
    except:
        raise FileNotFoundError("File not found")
    
def filtering_json(data:dict, filter_age:int , position:str):
    """Filtering JSON file by the given criterias"""
    if not data or not filter_age or not position:
       raise ValueError("Not valid parameters")
    
    set_of_positions={"Software Engineer", "Manager","Data Analyst","Manager","Graphic Designer","Project Manager"}   
    if not isinstance(filter_age,int) or not 0<filter_age<100:
       raise ValueError("Not valid age")
    if not isinstance(position,str) or  not position in set_of_positions :
       raise ValueError("Not valid position")
   
    main_key="users"
    if data.get(main_key):
       lst_users=data.get(main_key)
       res=[]
       filtered_dict={}
       for dicts in lst_users:
           if dicts.get("age")<=filter_age and dicts.get("position")==position:
              res.append(dicts)
              # dict with users which are matching the given criterias
              filtered_dict[main_key]=res
       return filtered_dict
           
    else:
        raise ValueError("Not valid data")
              

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
    if isinstance(raw_json,dict):
       f_name=validate_file_name(file_name)
       try:
           file=open(f_name,"x")
           json.dump(raw_json,file, indent=2)
           print("Succesfully done!")
           file.close()
       except:
           raise FileExistsError(f"File {f_name} already exists")
    else:
        TypeError("Not valid type for converting to JSON")             
           
def main():  
    file_path="user_data.json"
    data_json=parse_json(file_path)
    filter_age=35
    position="Manager"
    data=filtering_json(data_json, filter_age,position)
    process_to_JSON(data, "filtered_users")
        
    
if __name__=="__main__":
    main()
