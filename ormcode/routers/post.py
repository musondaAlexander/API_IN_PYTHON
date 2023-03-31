from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from mymodels import models
from mymodels.schemas import Post, CreatePost, PostResponse
from database import get_db
from typing import List
import auth2


# code to create a router object
router = APIRouter(
    prefix="/posts", # this is used to prefix the path operations.
    tags=["Posts"],# this is used to group the path operations.
)

#==================================================================================================== 
# Using a model to get post all the posts
@router.get("/", status_code=200, response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     return posts
# ===================================================================================
# Using a model to create a post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: CreatePost, db: Session = Depends(get_db), user_id: int = Depends(auth2.get_current_user)):
#   new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# ===================================================================================
# get single post 
@router.get("/{id}", status_code=200 , response_model=PostResponse)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    return post
# ===================================================================================
# update a post using a model
@router.put("/{id}" , status_code=status.HTTP_202_ACCEPTED, response_model=PostResponse)
def update_post(id: int, post: CreatePost, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == id)
    if not db_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    db_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return db_post.first()
# ===================================================================================
# delete a post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id {id} is not available")
    post.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"
