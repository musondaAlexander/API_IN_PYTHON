from database import get_db
from database import  engine
import time
import psycopg2  
from typing import Optional, Union
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from mymodels import  models, models
from mymodels.schemas import Post, CreatePost

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()


        
# Using a model to get post all the posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     return posts

# Using a model to create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: CreatePost, db: Session = Depends(get_db)):
#   new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# get single post 
@app.get("/posts/{id}", status_code=200)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    return post

# update a post using a model
@app.put("/posts/{id}" , status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, post: CreatePost, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == id)
    if not db_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    db_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"data": db_post.first(), "message": "updated successfully"}

# delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    post.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"


