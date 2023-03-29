from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from mymodels.schemas import UserLogin
from mymodels import models
import utils
import auth2

router = APIRouter(
    tags=["Authentications"]
    )

@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    
    #Create a tocken for the user
    access_token = auth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

    