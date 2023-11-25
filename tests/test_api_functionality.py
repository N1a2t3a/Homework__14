import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест для перевірки статусу відповіді на запит GET /
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Тест для перевірки створення нового контакту через POST /contacts/
def test_create_contact():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "123456789",
        "birthday": "1990-01-01"
    }
    response = client.post("/contacts/", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "johndoe@example.com"

# Тест для перевірки отримання списку всіх контактів через GET /contacts/
def test_read_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тест для отримання конкретного контакту за ідентифікатором через GET /contacts/{contact_id}
def test_read_contact():
    contact_id = 1
    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    assert response.json()["id"] == contact_id

# Тест для оновлення контакту за ідентифікатором через PUT /contacts/{contact_id}
def test_update_contact():
    contact_id = 1  
    data = {
        "first_name": "Updated",
        "last_name": "Name",
        "email": "updated@example.com",
        "phone_number": "987654321",
        "birthday": "1995-01-01"
    }
    response = client.put(f"/contacts/{contact_id}", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

# Тест для видалення контакту за ідентифікатором через DELETE /contacts/{contact_id}
def test_delete_contact():
    contact_id = 1  
    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 200
    assert response.json()["id"] == contact_id

