from fastapi import FastAPI, Depends, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from .models import User
from .database import get_db
import secrets 
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

# Параметри для генерації та перевірки токенів
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Встановлення контексту для хешування паролів
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

# Функція для генерації JWT токена доступу
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Функція для аутентифікації користувача та генерації токенів
@app.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    if not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Генерація JWT токенів
    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})

    return {"access_token": access_token, "refresh_token": refresh_token}