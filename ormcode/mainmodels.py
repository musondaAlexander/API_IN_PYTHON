# ====================================================================================================
# All the imports needed for the App 
from database import get_db
from database import  engine
import time
import psycopg2  
from typing import Optional, Union, List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from mymodels import  models, models
import utils
from mymodels.schemas import Post, CreatePost, PostResponse, CreateUser, UserResponse

# ====================================================================================================

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()

#==================================================================================================== 
# Using a model to get post all the posts
@app.get("/posts", status_code=200, response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     return posts
# ===================================================================================
# Using a model to create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: CreatePost, db: Session = Depends(get_db)):
#   new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# ===================================================================================
# get single post 
@app.get("/posts/{id}", status_code=200 , response_model=PostResponse)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    return post
# ===================================================================================
# update a post using a model
@app.put("/posts/{id}" , status_code=status.HTTP_202_ACCEPTED, response_model=PostResponse)
def update_post(id: int, post: CreatePost, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == id)
    if not db_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    db_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return db_post.first()
# ===================================================================================
# delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    post.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"
# ===================================================================================
# code for the user model
@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # hash the password before storing it in the database
    hashed_password = utils.hashing_password(user.password)
    user.password = hashed_password
    new_User = models.User(**user.dict())
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    
    return new_User
# ===================================================================================
# path operation for getting one user
@app.get("/users/{id}", status_code=200 , response_model=UserResponse)
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

# ===================================================================================


