import requests
import json


def fetch_data(URL_address,user_id:int):
    """ Sends a GET request to the URL. Retrieves posts by a specific user by adding a query parameter."""
    if not isinstance(user_id,int) or user_id<=0:
       raise ValueError("Not valid user ID")
    try:
          params={"userId":user_id}
          response=requests.get(URL_address,params=params)
          #checking status code
          if response.status_code !=200:
              print(f"Failed to fetch data: {response.status_code}")
              return  
          data_user_id_1=response.text
          data = json.loads(data_user_id_1)
          return data        
    except requests.exceptions.RequestException as e:
          print(f"An error occured: {e}") 

def post_json(URL_address,data:dict):  
    """Posts JSON file"""
    if not data:
       raise ValueError("Not valid json")
    try:
        response=requests.post(URL_address,json=data)
       
        # print check if an error has occurred
        if  response.status_code !=201:#201 denote successful response for POST
            print(f"Failed POST: {response.status_code}")
            return
        else:
            print("Posted")
    except requests.exceptions.RequestException as e:
          print(f"An error occured: {e}") 
    

def filter_json(user_id:int, find_element:str,data:dict)->None:
    """Parses the JSON response and print the titles of the posts."""
    result=[]
    for elements in data:
        if isinstance(elements,dict):
           if isinstance(find_element,str):
              if find_element.replace(" ",""):
                 result.append(elements.get(find_element))
              else:
                  raise ValueError("Not valid value to find")
        else:
           raise TypeError("Not valid data")
       
    print("_______Titles_______")       
    for i in result:
        print(f"{i} \n") 
       
          
def main():      
   link="https://jsonplaceholder.typicode.com/posts"
   user_id=1
   find_element="title"
   data=fetch_data(link, user_id)
   filter_json(user_id,find_element,data)
   
   json_data={
  "title": "Sample Post Title",
  "body": "This is the content of the post. It contains details about the topic or information being shared.",
  "userId": 123
   }
   
   post_json(link,json_data)
   
   

if __name__=="__main__":
   main()