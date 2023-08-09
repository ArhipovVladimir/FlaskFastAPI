"""Задание №8
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован."""


from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from hashlib import sha256, pbkdf2_hmac
import os

from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = b'6839b6fed8acf1fdb2ebf7e0cd1847f2db13de12ae2ca2467694c477824b3cec'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///userspassecr.db'
db.init_app(app)

@app.route('/')
def index():
    return "Users DB Sectet Password"


@app.cli.command("init-dbsuser")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username =form.username.data
        name =form.name.data
        surname =form.surname.data
        email = form.email.data
        open_password = form.password.data
        spasswd = sycretpass(open_password)
        print(spasswd)
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            error_msg = 'Username or email already exists.'
            form.username.errors.append(error_msg)
            return render_template('register.html', form=form)
        new_user = User(username=username, name=name, surname=surname, email=email, password=spasswd)
        db.session.add(new_user)
        db.session.commit()

        # Выводим сообщение об успешной регистрации
        success_msg = 'Registration successful!'
        return success_msg

    return render_template('register.html', form=form)


def sycretpass(password):

    # Пример генерации
    salt = os.urandom(32)
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Хранение как
    storage = salt + key
    # Получение значений обратно
    salt_from_storage = storage[:32]  # 32 является длиной соли
    key_from_storage = storage[32:]
    return storage



