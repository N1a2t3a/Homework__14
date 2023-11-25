from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'  
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()  
    contact_list = []
    for contact in contacts:
        contact_data = {
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone
        }
        contact_list.append(contact_data)
    return jsonify({'contacts': contact_list})

if __name__ == '__main__':
    db.create_all()  
    app.run(debug=True)