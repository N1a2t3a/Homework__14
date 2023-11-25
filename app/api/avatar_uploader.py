from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from cloudinary.uploader import upload
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    avatar = db.Column(db.String(200)) 

@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    if request.method == 'POST':
        user_id = request.form['user_id']
        image_file = request.files['image']
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'Користувач не знайдений'})

        # Завантаження файлу аватара на Cloudinary
        result = upload(image_file, folder='avatars')
        user.avatar = result['url']
        db.session.commit()

        return jsonify({'message': 'Аватар оновлено', 'avatar_url': user.avatar})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)