import time
import psycopg2  
from typing import Optional, Union
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

from psycopg2.extras import RealDictCursor



host = "localhost"
databse = "fastApiDb"
user = "postgres"
password = "flames####"

# connect to the database
while True:
    try:
        connect = psycopg2.connect(host=host, database=databse, user=user, password=password, cursor_factory=RealDictCursor)
        print("Database is connected")
        cursor = connect.cursor()
        break
    except Exception as errro:
        print("Database is not available. Trying to connect again...")
        print(errro)
        time.sleep(5)

   

# create a app instance
app = FastAPI()


# Using a model to create a post
class Post(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    

list_post =[{"title":"flames blog","body":"this is my first post","published":True, "id":1},
            {"title":"my second post","body":"this is my second post","published":True, "id":2},
            {"title":"my third post","body":"this is my third post","published":True, "id":3}]





#  fucntion to find a post by id
def find_post(id:int):
    for post in list_post:
        if post["id"] == id:
            return post
    return None

@app.get("/")
def read_root():
    return {"Hello": "Welcome To the Blog API Created By Alexander Musonda"}


@app.get("/posts")
def read_user_me():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"posts": posts}

# lets create a post request to add a user to the list of users
@app.post("/users")
def create_user(user_id: dict =  Body(...)):
    print(user_id)
    return {"user_id":user_id}


#updated the post request to add an id field ti list_post list 
# and return the post    

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    connect.commit()
    return {"post": new_post}


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
            return status.HTTP_204_NO_CONTENT
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

# the following method is the update method

@app.put("/posts/{id}", status_code= status.HTTP_200_OK)
def updatepost(id:int, post:Post):
        post1 = find_post(id)
        if post1 in list_post:
            list_post.remove(post1)
            updatedpost =  post.dict()
            updatedpost["id"] = id
            list_post.append(updatedpost)
            return {"message":list_post}  
        else:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Post not found")
