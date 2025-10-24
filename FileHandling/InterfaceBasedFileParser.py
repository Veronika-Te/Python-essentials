import os
from abc import ABC, abstractmethod
import csv
import json

class IFileParser(ABC):
  @abstractmethod
  def parse(self, filepath: str):
    """
    Parse the given file and return its content.
    What to return depends on the file type:
    - CSV → list of dictionaries (one per row)
    - JSON → Python object (dict or list)
    - TXT → list of lines (strings)
    """
    pass
  
  @abstractmethod
  def file_type(self) ->str:
    """
    Return the file type handled by the parser (e.g., 'CSV', 'JSON', 'TXT').
    """
    pass


class CSVParser(IFileParser):
  def parse(self, filepath: str) -> list[dict]:
    data=[]
    try:
      with open(filepath, mode='r', encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
          data.append(row)
    except FileNotFoundError:
      print(f"Error: CSV file not found at {file}")
      return []
    except Exception as e:
      print(f"Error parsing CSV file {file}: {e}")
      return []
    return data
  
  def file_type(self) ->str:
    return 'CSV'
  
class JSONParser(IFileParser):
  def parse(self, filepath: str):
    try:
      with open(filepath,mode='r',encoding='utf-8') as file:
        content=json.load(file)
    except FileNotFoundError:
      print(f"Error: JSON file not found at {filepath}")
      return 
    except json.JSONDecodeError as e:
      print(f"Error decoding JSON file {filepath}: {e}")
      return 
    except Exception as e:
      print(f"Error parsing JSON file {filepath}: {e}")
      return 
    return content
  
  def file_type(self) ->str:
    return 'JSON'
  
class TXTParser(IFileParser):
  def parse(self, filepath:str) -> list[str]:
    lines=[]
    try:
      with open(filepath, mode='r', encoding='utf-8') as file:
        lines=[line.strip() for line in file]
    except FileNotFoundError:
      print(f"Error: TXT file not found at {filepath}")
      return []
    except Exception as e:
      print(f"Error parsing TXT file {filepath}: {e}")
      return []
    return lines
  
  def file_type(self) ->str:
    return 'TXT'
  
  
def process_file(parser: IFileParser, filepath:str):
  """
  Takes an IFileParser implementation and a filepath,
  then parses the file and prints its content.
  """
  print(f"\n--- Processing {parser.file_type()} file: {filepath} ---")
  content = parser.parse(filepath)
  #print(content)
  if content is not None:
    print(f"Content for {parser.file_type()} {type(content)}) @@")
    if parser.file_type() == 'TXT':
      for line in content:
        print(f" {line}")
    else:
      print(json.dumps(content, indent=2))
      
  else:
    print("Failed to parse file.")
  
      
if __name__=="__main__":
  base_dir = os.path.dirname(__file__)  # Folder of this script
  data_path = os.path.join(base_dir, "data")
  print(base_dir)
  print(data_path)
  
  if not os.path.exists(data_path):
    print("Data folder not found!")
  else:
    print(f"Data folder exists: {data_path}")  
  
  csv_parser = CSVParser()
  json_parser = JSONParser()
  txt_parser = TXTParser()
  
  parsers = [csv_parser, json_parser, txt_parser]
  filepaths = {
      'CSV': f"{data_path}/sample.csv",
      'JSON': f"{data_path}/sample.json",
      'TXT': f"{data_path}/sample.txt"
    }
  
  for parser in parsers:
    process_file(parser, filepaths[parser.file_type()])

  
  
  
  