from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Contact, ContactCreate, ContactUpdate, User
from .database import get_db
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

@app.post("/contacts/", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if contact.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this contact")
    
    db_contact = Contact(**contact.dict())
    db_contact.owner_id = current_user.id
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    if db_contact.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this contact")
    
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.delete("/contacts/{contact_id}", response_model=Contact)
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    if db_contact.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this contact")
    
    db.delete(db_contact)
    db.commit()
    
    return db_contact