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
from mymodels.schemas import Post

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()


        
# Using a model to create a post
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     return posts

# method to add a single post to the database
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(title=post.title, content=post.content, published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


