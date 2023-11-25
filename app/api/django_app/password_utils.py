from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

# Ініціалізація серіалізатора
serializer = URLSafeTimedSerializer('your_secret_key_here')

# Генерація токену для скидання паролю
def generate_reset_token(email):
    return serializer.dumps(email, salt='password-reset-salt')

# Перевірка та отримання email з токену
def verify_reset_token(token, expiration=3600):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        return email
    except:
        return None

# Надсилання листа з посиланням для скидання паролю
def send_reset_email(mail, email, token):
    reset_link = url_for('reset_password', token=token, _external=True)
    msg = Message('Скидання паролю', sender='your_email@example.com', recipients=[email])
    msg.body = f'Для скидання паролю перейдіть за посиланням: {reset_link}'
    mail.send(msg)