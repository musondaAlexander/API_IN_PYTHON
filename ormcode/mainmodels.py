# ====================================================================================================
# All the imports needed for the App
from database import get_db
from database import engine
import time
import psycopg2
from typing import Optional, Union, List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from mymodels import models, models
import utils
from mymodels.schemas import Post, CreatePost, PostResponse, CreateUser, UserResponse
from routers import post, user

# ====================================================================================================

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
