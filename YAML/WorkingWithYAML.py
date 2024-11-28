import yaml
import json

class ModifierYaml:
    def __init__(self,path)->None:
        self.path=path
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, value):
        if not value:
            raise ValueError("Empty path")
        if isinstance(value,str):
            if value.replace(" ",""):
               self.__path=value
            else:
                raise ValueError("Not valid path")
        else:
            raise TypeError("Not valid type for path value")
    

    def _read_log_file(self)->dict:
        """Reads YAML file"""
        try:
            with open (self.path,"r") as file:
                data=yaml.safe_load(file)
                return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error! The {file} Not found; {e}")
    
    def change_data_YAML(self, key: str, key2:str, value_key2:int)->None:
        """Modifies data by the key"""
        data=self._read_log_file()
        if not data:
           raise ValueError("Empty file")
        if data.get(key, {}):
           if data.get(key, {}).get(key2):   
               #set value to port
              data[key][key2]=value_key2
              print(f" Message: Changed {key2} value is {data[key][key2]}")
           else:
              raise ValueError(f"Not valid inner key: {key2}")
        else:
             raise ValueError(f"Not valid key: {key}")  
        
    def convert_to_json(self):
        """Converts to JSON and writes to the file"""
        data=self._read_log_file()
        try:
           #in "x" mode in order not to lose data if it already exists
           file=open("data.json",'x')
           #writes to new file called data.json
           json.dump(data,file, indent=2)
           file.close()
        except TypeError as e:
              # non-serializable object. 
               raise TypeError(f"JSON encoding error; {e}")
        except FileExistsError as e:
               raise FileExistsError(f"Error {file} already exists; {e}") 
        except Exception as e:
               raise Exception(str(e))
        
    
               
def main()->None:
    try:
        path="config.yaml"
        my=ModifierYaml(path)
        #value to change
        key='server'
        key2='port'
        value_key2=9090
        my.change_data_YAML(key, key2,value_key2)
        #converting to JSON
        my.convert_to_json()
    except Exception as e:
        print(e)
    
if __name__=="__main__":
   main()
