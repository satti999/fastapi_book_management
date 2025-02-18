from sqlmodel import Session, select
from fastapi import Depends
import redis
from models.user_model import User
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class UserController:
  def __init__(self, db,redis_client: redis.Redis):
        self.redis = redis_client
        self.db = db
   
  def sign_up(self, user):
        email=user.email
        password=user.password
        existing_user=self.db.exec(select(User).filter(User.email==email).first())
        if existing_user:
            return JSONResponse(content={"message": "User already exists"}, status_code=400)
        if len(password)<8:
            return JSONResponse(content={"message": "Password must be at least 8 characters"}, status_code=400) 
        self.redis.setex(email, 3600, user)    
        return JSONResponse(content={"message": "OTP sent successfully"}, status_code=200)
   
  def login(self, user: User):
       existing_user=self.db.exec(select(User).filter(User.email==user.email).first())
       if  existing_user:
          if  existing_user.password== user.password:
            JSONResponse(content={"message": "User logged in successfully","data":user}, status_code=200)
          else:
            return JSONResponse(content={"message": "Incorrect password"}, status_code=400)     
       else:
           return JSONResponse(content={"message": "User not found"}, status_code=404)
       
  def verify_otp(self,user_otp,email):
      user=User(**jsonable_encoder(self.redis.get(email)))
      otp=user_otp
      email=user.email
      if otp==user_otp:
          self.db.add(user)
          self.db.commit()
          self.db.refresh(user)
          self.redis.delete(email)
          return JSONResponse(content={"message": "user created successfully","data":user}, status_code=200)
      else:
          return JSONResponse(content={"message": "Invalid OTP"}, status_code=400)
       
    
