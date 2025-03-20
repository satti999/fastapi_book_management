from sqlmodel import Session, select
from fastapi import Depends
import redis
import json
from models.user_model import User
from utils.email_support import send_email,generate_email_body
from utils.generate_otp import generate_otp
from utils.jwt_token import create_jwt,verify_jwt
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from utils.hash_password import get_password_hash,verify_password


class UserController:
  def __init__(self, db,redis_client: redis.Redis):
        self.redis = redis_client
        self.db = db
   
  def sign_up(self, user):
        email=user.email
        print("email",email)
        password=user.password
        existing_user=self.db.exec(select(User).filter(User.email==email).first())
        if existing_user:
            return JSONResponse(content={"message": "User already exists"}, status_code=400)
        if len(password)<8:
            return JSONResponse(content={"message": "Password must be at least 8 characters"}, status_code=400)
        otp=generate_otp() 
        new_user={
            "username":user.username,
            "email":user.email,
            "password":user.password,
            "otp":otp

        }
        self.redis.setex(email, 3600, json.dumps(new_user))
        email_body=generate_email_body(otp)
        email_send=send_email(user.email,"OTP Verification",email_body)
        if not email_send:
            return JSONResponse(content={"message": "Email not sent"}, status_code=400)   
        return JSONResponse(content={"message": "OTP sent successfully"}, status_code=200)
   
  def login(self, user: User):
       existing_user=self.db.exec(select(User).filter(User.email==user.email).first())
       if  existing_user:
         if not verify_password(user.password,existing_user.password):
            return JSONResponse(content={"message": "Invalid password"}, status_code=400)
         else:
            token=create_jwt(existing_user.dict())
            return JSONResponse(content={"message": "Login successful","token":token}, status_code=200)        
       else:
           return JSONResponse(content={"message": "User not found"}, status_code=404)
       
  def verify_otp(self,user_otp,email):
      
      user_data=json.loads(self.redis.get(email))
      otp = user_data.get("otp")
      email=user_data.get("email")
      user_name=user_data.get("username")
      user_password=user_data.get("password")
      if otp==user_otp:
          hashed_password=get_password_hash(user_password)
          user=User(username=user_name,email=email,password=hashed_password)
          self.db.add(user)
          self.db.commit()
          self.db.refresh(user)
          self.redis.delete(email)
          return JSONResponse(content={"message": "user created successfully","data":user}, status_code=200)
      else:
          return JSONResponse(content={"message": "Invalid OTP"}, status_code=400)
       
    
