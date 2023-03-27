
from pydantic import BaseModel, EmailStr
from pyparsing import Optional
from datetime import datetime

# ====================================================================================================
# Using a model to create a post


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# This will handle both create and update


class CreatePost(Post):
    pass
# ====================================================================================================
# class for a response:


class PostResponse(Post):
    id: int
    created_at: datetime

    class Config:  # This will allow us to create a response model
        orm_mode = True
# ====================================================================================================
# Schema for users

class CreateUser(BaseModel):
    email: EmailStr
    password: str
    
# ====================================================================================================
# class for a response for users
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:  # This will allow us to create a response model
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
