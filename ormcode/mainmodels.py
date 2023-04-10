# ====================================================================================================
# All the imports needed for the App
from database import engine
from fastapi import  FastAPI
from mymodels import models, models
from routers import post, user, auth

# ====================================================================================================

models.Base.metadata.create_all(bind=engine)

# creatin a app instance
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
