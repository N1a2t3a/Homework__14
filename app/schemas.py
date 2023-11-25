from pydantic import BaseModel
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    additional_data: str = None


class ContactUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    birthday: str = None
    additional_data: str = None
    