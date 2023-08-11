"""Пробное решение диплома"""


from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from hashlib import sha256, pbkdf2_hmac
import os

from forms import ProcessForm
from models import db, Reestr, Process

app = Flask(__name__)
app.config['SECRET_KEY'] = b'6839b6fed8acf1fdb2ebf7e0cd1847f2db13de12ae2ca2467694c477824b3cec'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///fincontrol.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')


@app.cli.command("init-dbfk")
def init_db():
    db.create_all()


@app.route('/process/', methods=['GET', 'POST'])
def register():
    form = ProcessForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        if not request.form['name']:
            flash('Введите процесс!', 'danger')
            return redirect(url_for('form'))

        new_proc = Process(name=name)
        db.session.add(new_proc)
        db.session.commit()
        flash(f'Процесс зарезистрирован', 'success')
        return redirect(url_for('form'))
        # Выводим сообщение об успешной регистрации
        # success_msg = 'Registration successful!'
        # return success_msg

    return render_template('process.html', form=form)


# def form():
#     if request.method == 'POST':
#         # Проверка данных формы
#         if not request.form['name']:
#             flash('Введите имя!', 'danger')
#             return redirect(url_for('form'))
#     # Обработка данных формы
#         name = request.form.get('name')
#         flash(f'Привет {name}', 'success')
#         return redirect(url_for('form'))
#
#     return render_template('form.html')



@app.route('/processget/')
def all_process():
    process = Process.query.all()
    context = {'process': process}
    return render_template('processget.html', **context)





