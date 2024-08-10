import json
#Opening JSON file
with open("hello.json", "r") as read_content: 
    print(json.load(read_content))
#{'name': 'Frieda', 'isDog': True, 'hobbies': ['eating', 'sleeping', 'barking'], 'age': 8, 'address': {'work': None, 'home': ['Berlin', 'Germany']}, 'friends': [{'name': 'Philipp', 
#'hobbies': ['eating', 'sleeping', 'reading']}, {'name': 'Mitch', 'hobbies': ['running', 'snacking']}]}   
  
#Convert Python Dictionaries to JSON
food_ratings = {"dog food": 2, "human food": 10}
file=json.dumps(food_ratings)
print(file)
