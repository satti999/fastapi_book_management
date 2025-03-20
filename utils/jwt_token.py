from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_jwt(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    """ Generate a JWT token with expiration. """
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    payload = data.copy()
    payload.update({"exp": expire})
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt(token: str):
    """ Verify and decode a JWT token. """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None  # Invalid token

