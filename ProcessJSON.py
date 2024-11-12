import json
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
    # Define the JSON data
    raw_json = {
        "company": "TechCorp",
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"id": 1, "name": "Alice", "role": "Engineer"},
                    {"id": 2, "name": "Bob", "role": "Manager"}
                ]
            },
            {
                "name": "Sales",
                "employees": [
                    {"id": 3, "name": "Charlie", "role": "Sales Rep"},
                    {"id": 4, "name": "Dana", "role": "Sales Lead"}
                ]
            }
        ]
    }
    
    #JSON file name(give it without ".json" extension)
    str_name="company_data"
    process_to_JSON(raw_json,str_name)

if __name__ == "__main__":
    main()