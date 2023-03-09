
from pycodestyle import BaseModel
from pyparsing import Optional


# Using a model to create a post
class Post(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    