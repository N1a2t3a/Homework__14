from sqlalchemy.orm import Session
from .models import BaseModel, Contact
from . import models
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

def search_contacts(db: Session, query: str):
    query = f"%{query}%"  
    contacts = db.query(models.Contact).filter(
        (models.Contact.first_name.ilike(query)) |
        (models.Contact.last_name.ilike(query)) |
        (models.Contact.email.ilike(query))
    ).all()
    return contacts

# Додавання нового контакту
def create_contact(db: Session, contact: models.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

# Отримання списку всіх контактів
def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()

# Отримання контакту за ідентифікатором
def get_contact(db: Session, contact_id: int):
    return db.query(BaseModel).filter(BaseModel.id == contact_id).first()

# Оновлення існуючого контакту
def update_contact(db: Session, contact_id: int, contact: models.ContactUpdate):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact:
        for key, value in contact.dict().items():
            setattr(db_contact, key, value)
        db.commit()
    return db_contact


# Видалення контакту
def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact