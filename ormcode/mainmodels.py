from database import  engine,Sessionlocal
import time
import psycopg2  
from typing import Optional, Union
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from mymodels import  models, models

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()


# create a depe
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
# Using a model to create a post
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     return posts

