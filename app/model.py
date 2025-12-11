from .database import Base
from pydantic import BaseModel
from sqlalchemy import String, Integer, Column
from typing import List


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False )
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)


class UserCreate(BaseModel):
    username : str
    password : str
    email : str


class UserVerify(BaseModel):
    username : str
    password : str


class UserResponse(UserCreate):
    id : int

class AnalyzeSchema(BaseModel):
    resume : str
    ton : str
    categorie : str
    score : float



class AnalyzeRequest(BaseModel):
    text: str
    candidate_labels: List[str]