from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    cover_image: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    cover_image: Optional[str] = None

    class Config:
        from_attributes = True