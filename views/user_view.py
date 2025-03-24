from fastapi import APIRouter, Depends

from controller.user_controller import UserController
from schema.user_schema import UserCreate, UserResponse
from sqlmodel import Session
from database.db_connection import get_session
from dependencies.redis_dependency import get_redis


router = APIRouter()


@router.post("/sign-up")
def signup_user(user: UserCreate, db: Session = Depends(get_session()),redis_client=Depends(get_redis)):
    controller = UserController(db,redis_client)
    return controller.sign_up(user)


@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_session())):
    controller = UserController(db)
    return controller.login(user)
3