import os  
def write_file(file_name):
    """Creates a text file in write mode"""
    try: 
       file=open(file_name,'w')
       file.write("Hello.")
       return f"Success, file '{file_name}' was created"
    finally:
       file.close()

def read_file(file_name):
    """Opens the text file in read mode"""
    try:
       file=open(file_name,'r')
       text=file.read()
       return text
    finally: 
       file.close()

def append_line_to_file(file_name,line)->str:
    """Apppend the line to text file"""
    try:
      file=open(file_name,'a')
      text=file.write(line)
      return f"Success, To '{file_name}' file was appended new line"
    finally:
      file.close()
    
        
def delete_file(file_name:str)->str:
    """Delete the file"""  
    file_name = 'mytxt.txt'
    os.remove(file_name)
    return (f"File '{file_name}' deleted successfully.")

          
def get_keys(dictionary:dict)->set:
    """Creates set with keys of the given dictionary"""
    if not dictionary: 
       return
    return set(dictionary.keys())


def file_manager(file_name:str, operation:str, content=None)->str:
    """Uses this dictionary to perform the requested file operation."""
    file_operations={'Write':write_file ,'Read':read_file , 'Append line':append_line_to_file, 'Delete':delete_file}
    keys_set=get_keys(file_operations)  
    
    if not file_name or not operation:
        return "Missing arguments"
    if operation in keys_set:
        if operation=='Write':
           write=file_operations.get(operation)
           return write(file_name)
        elif operation=='Append line':
           appended=file_operations.get(operation)
           return appended(file_name, content)
        elif operation=='Read':
           read=file_operations.get(operation)
           return read(file_name)
        elif operation=='Delete':
           delete=file_operations.get(operation)
           return delete_file(file_name)
        else:
           return "Unknown operation"
    else:
        return "Unknown operation"
          
    
def main()->None:
   
   print("________File manager_________")
   
   try:

   #Write
      file_name='mytxt.txt'
      line="How are you?"
      operation1='Write'
      w=file_manager(file_name, operation1)
      print(w)
   #Appended
      operation2='Append line'
      a=file_manager(file_name, operation2, content=line)
      print(a)
   #Read
      operation3='Read'
      r=file_manager(file_name, operation3)
      print(r)
   #Delete
      operation4='Delete'
      d=file_manager(file_name,operation4)
      print(d)
   except IOError as e:
      print("Failed")
 
if __name__=="__main__":
   main()
    