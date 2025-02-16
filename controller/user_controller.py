from sqlmodel import Session, select
from ..models.user_model import User
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class UserController:
   def __init__(self, db):
        self.db = db
    
   def sign_up(self, user):
        email=user.email
        password=user.password
        existing_user=self.db.exec(select(User).filter(User.email==email).first())
        if existing_user:
            return JSONResponse(content={"message": "User already exists"}, status_code=400)
        if len(password)<8:
            return JSONResponse(content={"message": "Password must be at least 8 characters"}, status_code=400)    
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        user=jsonable_encoder(user)
        return JSONResponse(content={"message": "User created successfully","data":user}, status_code=200)
   
   def login(self, user: User):
       existing_user=self.db.exec(select(User).filter(User.email==user.email).first())
       if  existing_user:
          if  existing_user.password== user.password:
            JSONResponse(content={"message": "User logged in successfully","data":user}, status_code=200)
          else:
            return JSONResponse(content={"message": "Incorrect password"}, status_code=400)     
       else:
           return JSONResponse(content={"message": "User not found"}, status_code=404)
