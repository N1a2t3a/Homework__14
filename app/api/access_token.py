from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from .database import get_db
from .models import User
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

def get_current_user(db: Session = Depends(get_db), token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=400, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return db_user