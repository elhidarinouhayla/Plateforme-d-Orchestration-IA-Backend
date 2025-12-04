from database import Base
from pydantic import BaseModel
from sqlalchemy import String, Integer, Column


class User():
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False )
    password = Column(String, nullable=False)


class UserCreate(BaseModel):
    id : int
    username : str
    password : str

class UserResponse(UserCreate):
    id : int


