
from pydantic import BaseModel
from pyparsing import Optional


# Using a model to create a post
class Post(BaseModel):
    title: str
    content: str
    published: bool
    
# This will handle both create and update
class CreatePost(Post):
    pass
    