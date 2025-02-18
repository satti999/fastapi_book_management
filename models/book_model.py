from sqlmodel import SQLModel, Field, Relationship
from models.user_model import User
from typing import Optional

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    author: str
    description: Optional[str] = None
    cover_image: Optional[str] = None
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="books")