from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
import requests
import httpx

app = FastAPI()

#for post
# users = 
#     {
#        "id": 1,
#        "name": "Alice"
#     },
#     {   
#        "id": 2, 
#        "name": "Bob"
#    }


class UserModel(BaseModel):
    id : int
    name: str
 
#empty list to store users
users=[]

#Route for the home page
@app.get("/users")
def welcome():
    return {'message': 'Welcome to my FastAPI application using CRUD'}

#Route to create a new article
#The response model specifies that the response  will be a "UserModel" object
@app.post("/users", response_model=list[UserModel])
async def create_user(user_lst:list[UserModel]):
    if not user_lst:
       raise HTTPException(status_code=400, detail="No users provided")  # Handle empty input
    for u in user_lst:
        users.append(u) #Add  the deserialized UserModel object directly
    return users


#Route to get user by soecific id
#The response model specifies that the response  will be a "UserModel" object
@app.get("/users", response_model=UserModel)
async def read_users(user_id:int):
    if  user_id is not None:  # If a specific user ID is provided
        user=None
        for u in users:
            if u["id"] == user_id:
                user = u  #found by key id
                break
        if user is None:
            raise HTTPException(status_code=404, detail=f"User ID:{user_id} not found")
        return [user]  # Return as a list for compatibility with `response_model`
    return users  # Return all users if no ID is specified
       


#Route and update existing user by its ID
#The response model specifies that the response  will be a "UserModel" object
@app.put("/users/{user_id}", response_model=UserModel)
async def update_user(user_id:int, updated_user:UserModel):
    for index, user in enumerate(users):
        if user.id==user_id: #check in our list of usermodels 
           users[index] = updated_user
           return updated_user
    raise HTTPException(status_code=404, detail=f"User ID:{user_id}not found")
   

#Route to delete an user by it's ID
@app.delete("/users/{user_id}")
async def delete_user(user_id:int):
     for index, user in enumerate(users):
         if user.id == user_id:
            del users[index]#Deletes the user from the list
            return {"message": "User deleted"}
     raise HTTPException(status_code=404, detail=f"User ID:{user_id}not found")


def run():
    import uvicorn
    try:
        HOST="127.0.0.1"
        PORT=8000
        # Start the server
        uvicorn.run("CRUD_users:app", host=HOST, port=PORT, reload=True, log_level=2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()
    