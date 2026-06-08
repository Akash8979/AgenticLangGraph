from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


# simaple get api 

@app.get("/")
def home():
    return {"message": "Hello World"}


# get with an endpoint name
@app.get("/about")
def about():
    return {"message":"this is about api"}



#get api with path parameter
@app.get("/user/{user_id}")
def get_user_details(user_id:int):
    return {"user_id":user_id}


class User(BaseModel):
    name:str
    age:int



    """
    Base model is use to validate request body data ,
    type chacking
    Automatic parsing
    fast api user pytdentic internally
    """

# simple post api
@app.post("/users")
def create_user(user:User):
    return {
        "message":"user created",
        "data":user
        }


   
"""
To start fast api server command - uviconr main:app --host 0.0.0.0 --port 8000
"""   