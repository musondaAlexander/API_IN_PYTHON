from typing import Optional, Union
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()
# we are going to use a moel now to create some validations for our data

class Post(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

list_post =[{"title":"flames blog","body":"this is my first post","published":True, "id":1},
            {"title":"my second post","body":"this is my second post","published":True, "id":2},
            {"title":"my third post","body":"this is my third post","published":True, "id":3}]



#  fucntion to find the post by id
def find_post(id:int):
    for post in list_post:
        if post["id"] == id:
            return post
    return None

@app.get("/")
def read_root():
    return {"Hello": "Welcome to  Alexander's API"}


@app.get("/posts")
def read_user_me():
    return {"posts": list_post}

# lets create a posy request

@app.post("/users")
def create_user(user_id: dict =  Body(...)):
    print(user_id)
    return {"user_id":user_id}


#updated the post request to add an id field ti list_post list 
# and return the post    

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    new_post = post.dict()
    new_post["id"] = randrange(0,100)
    list_post.append(new_post)
    print(post)
    return {"post":post}


# get a single post 
@app.get("/singlepost/{id}")
def get_single_post(id:int):
    post = find_post(id)
    if post:
        return {"post":post}
    

# the follwing method is the Delete method
@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def deletepost(id:int):
        post = find_post(id)
        if post in list_post:
            list_post.remove(post)
            return {"message":post}

# the following method is the update method

# @app.update("/posts/{id}", status_code= status.HTTP_200_OK)
# def updatepost(id:int, post:Post):
#         post = find_post(id)
#         if post in list_post:
#             list_post.remove(post)
#             list_post.append(post)
#             return {"message":post}       