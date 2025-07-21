
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from . database import engine
from . routers import post, user, auth, vote
from . config import settings

# print(settings.database_password)



# models.Base.metadata.create_all(bind=engine)  # Create the database tables

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


        
app.include_router(post.router)  #Includes the post router
app.include_router(user.router)
app.include_router(auth.router) 
app.include_router(vote.router)  #Includes the user router
        

@app.get("/")  #Uses api endpoint
async def root():
    return {"message": "Hello World"}




