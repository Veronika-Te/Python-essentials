import json
#Opening JSON file
def open_JSON(file_name):
    try:
       with open(file_name, "r") as read_content: 
           return json.load(read_content)
    except IOError as e:
        return "Failed"
    
#Converting to JSON
def write_JSON(dictionary):
    file=json.dumps(food_ratings)
    return file

if __name__=="__main__":
  #open JSON
  file_name="hello.json"
  f=open_JSON(file_name)
  print(f)

  #Convert Python Dictionaries to JSON
  food_ratings = {"dog food": 2, "human food": 10}
  f1=write_JSON(food_ratings)
  print(f1)