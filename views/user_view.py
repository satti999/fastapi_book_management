from fastapi import APIRouter, Depends

from ..controller.user_controller import UserController
from ..schema.user_schema import UserCreate, UserResponse
from sqlmodel import Session
from ..database.db_connection import get_session


router = APIRouter()


@router.post("/user/sign-up")
def signup_user(user: UserCreate, db: Session = Depends(get_session())):
    controller = UserController(db)
    return controller.sign_up(user)


@router.post("/user/login")
def login_user(user: UserCreate, db: Session = Depends(get_session())):
    controller = UserController(db)
    return controller.login(user)