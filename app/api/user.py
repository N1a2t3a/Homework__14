from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import User
from sqlalchemy.orm import Session
from .database import get_db
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

class UserCreate(BaseModel):
    email: str
    password: str

@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Перевірка, чи користувач із таким email існує
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Хешування пароля
    hashed_password = bcrypt.hash(user.password)

    # Збереження користувача
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user