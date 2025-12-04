from fastapi import FastAPI,HTTPException,Depends
from database import Base,engine,get_db
from sqlalchemy.orm import session
from model import UserCreate, UserResponse, User
from auth import create_token, verify_token
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
Base.metadata.create_all(bind=engine)


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# creation d'un username :
@app.post("/register", response_model=UserResponse)
def create_user(user=UserCreate, db: session=Depends(get_db)):
    exist = db.query(User).filter(User.username == user.username).first()

    if exist:
        raise HTTPException(status_code=400, detail= "username existe deja")
    
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




