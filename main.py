from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import crud, schemas
from .database import get_db, engine
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

# Створення основного екземпляру FastAPI
app = FastAPI()

# Створення роутерів
router = APIRouter()

@router.get("/search/")
async def search_contacts(query: str, db: Session = Depends(get_db)):
    contacts = crud.search_contacts(db, query)
    if not contacts:
        raise HTTPException(status_code=404, detail="Contacts not found")
    return contacts

# Схема Pydantic для створення контакту
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    additional_data: Optional[str] = None

# Роут для створення нового контакту
@app.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact)

# Роут для отримання списку всіх контактів
@app.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contacts(db, skip=skip, limit=limit)

# Роут для отримання контакту за ідентифікатором
@app.get("/contacts/{contact_id}", response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    return crud.get_contact(db, contact_id=contact_id)

# Роут для оновлення контакту за ідентифікатором
@app.put("/contacts/{contact_id}", response_model=schemas.Contact)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)):
    return crud.update_contact(db=db, contact_id=contact_id, contact=contact)

# Роут для видалення контакту за ідентифікатором
@app.delete("/contacts/{contact_id}", response_model=schemas.Contact)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    return crud.delete_contact(db=db, contact_id=contact_id)

# Додавання роутера до основного екземпляру FastAPI
app.include_router(router, prefix="/api/v1")