import os

def setup_month(month:str, base_path: str):
  """Creates folder in existing directory""" 
  full_path=create_full_path(base_path, month)
  if not full_path:
    return
  if os.path.exists(full_path):
    print(f"Folder already exists")
  else:
    os.makedirs(month, exist_ok=True)
    print(f"Folder created at: {full_path}")

def add_note(month:str , day:int,  base_path: str, note:str="Empty note"):
  """Adds note with defiined day"""
  full_path_month = create_full_path(base_path, month)
  if not full_path_month:
    return
  if not isValid_day(day):
    return
  txt_ext=".txt"
  file_name=str(day) + txt_ext
  #print(file_name)
  if not isinstance(note, str):
    return
  full_path=os.path.join(full_path_month, file_name)
 
  with open(full_path, 'w') as file:
    file.write(note)

def create_full_path(base_path: str, month: str):
  """Creates full path for month"""
  if not month or not isinstance(month, str):
    return
  if not base_path or not os.path.exists(base_path):
    return
  months={"March", "April", "May", "June", "July", "August","September", "October", "November", "December", "January", "February"}
  if not month in months:
    return
  full_path = os.path.join(base_path, month)
  if not os.path.exists(full_path):
    return  
  return full_path
  
def isValid_day(day:int)->bool:
  """Checks if day value is valid"""
  min_day=1
  max_day=31
  if not day or not min_day<=day<=max_day:
    return False
  if not isinstance(day, int):
    return False
  return True
  
def read_note(month: str, day: int, base_path: str ) -> str:
  """Read the content of the note for a specific day.
  """
  try:
    full_path_month=create_full_path(base_path, month)
    if not full_path_month:
      return
    if not isValid_day(day):
      return
    txt_ext=".txt"
    file_name=str(day) + txt_ext
    full_path=full_path_month+"/"+file_name
    if not os.path.exists(full_path):
      raise FileNotFoundError(f"No note found for {month} {day}") 

    with open(full_path, 'r') as file:
      text=file.read()

    if not text:
      return "f{full_path} File is empty"
    return text
  except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
  except IOError as e:
        print(f"Error reading file: {e}")
        return None
  except Exception as e:
        print(f"Unexpected error in read_note: {e}")
        return None
 
def list_notes(month: str, base_path: str ) -> list[int]:
  """Return a list of day numbers (integers) for which notes exist in the month folder. """
  full_path_month=create_full_path(base_path, month)
  if not full_path_month:
    return
  files = os.listdir(full_path_month)
  #print(files)
  #print(type(files))
  if not files:
    return [0]
  return files

def delete_note(month: str, day: int, base_path:str) -> None:
  """Delete the note file for a specific day."""
  full_path_month=create_full_path(base_path, month)
  if not full_path_month:
    return
  if not isValid_day(day):
    return
  txt_ext=".txt"
  file_name=str(day) + txt_ext
  full_path=full_path_month+"/"+file_name
  if os.path.exists(full_path):
    os.remove(full_path)
    print(f"File {full_path} has been deleted.")
  else:
    print(f"The file {full_path} does not exist.")


def main():
  month="March"
  base_path="/Users/verterteryan/Projects_/Projects_AI/MonthlyNotesOrganizer"

  setup_month(month, base_path)
  
  try:
    add_note(month, 28,base_path)
    add_note(month, 20,base_path)
    add_note(month, 27,base_path)
    txt=read_note(month, 27, base_path)
    print(txt)
    list_notes(month, base_path)
    delete_note(month,20,base_path)
  except ValueError as e:
    print(f"Input error: {e}")
  except Exception as e:
    print(f"Error in main: {e}")

if __name__=="__main__":
  try:
    main()
  except Exception as e:
    print(e)

  