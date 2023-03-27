from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from mymodels import models
from mymodels.schemas import CreateUser, UserResponse
from database import get_db
import utils

# code to create a router object
router = APIRouter(
    prefix="/users", # this is used to prefix the path operations
    tags=["Users"],# this is used to group the path operations
)

# ===================================================================================
# code for the user model
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
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
@router.get("/{id}", status_code=200 , response_model=UserResponse)
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

# ===================================================================================
