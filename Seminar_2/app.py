"""
Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени."""


from flask import Flask, request, render_template, redirect, url_for, abort, flash
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename
from math import sqrt


app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/hello')
def hello1():
    return "Привет Мир!Й"

"""Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений."""

@app.route('/uploads/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static', file_name))
        return render_template('task2_1.html', file_name=file_name)
    return render_template('uploads.html')

"""
Задание №3
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""
users = {"admin": "123",
         "ivan": '15'}

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username, password)
        if (username, password) in users.items():
            return 'Вы вошли'
        return 'Ошибка логина или пароля'
    return render_template('login.html')

"""
Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""
@app.route('/count/', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        count = len(text.split(" "))
        return f'колличество слов {count}'
    return render_template('count1.html')

""" Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом."""

@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = int(request.form.get('number1'))
        number2 = int(request.form.get('number2'))
        print(number1, number2)
        operation = request.form.get('operation')
        if operation == "add":
            return f'{number1 + number2}'
        if operation == "subtract":
            return f'{number1 - number2}'
        if operation == "multiply":
            return f'{ number1 * number2}'
        if operation == "divide":
            return f'{number1 / number2}'
    return render_template('calc.html')

"""
Задание №6
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""
@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        username = request.form.get('username')
        age = int(request.form.get("age"))
        if age < 18:
            abort(403)

    return render_template('Age.html')

@app.errorhandler(403)
def age_age_not(e):
    app.logger.warning(e)
    context = {'title': 'возраст меньше 18',
                'url': request.base_url,
               }
    return render_template('403.html', **context), 403

"""
Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат."""

@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get("number"))
        result = sqrt(number)
        return redirect(url_for('sqr_result', result=result))
    return render_template("squar.html")


@app.route('/square/result')
def sqr_result():
    return request.args.get("result")

"""
Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!"."""

app.secret_key = '62e14179dd8dea918d1375fd65876e8568034827b5bee3a9f037ae36e3922ec4'
@app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#          name = request.form.get('name')
#          flash(f'Привет{name}', 'warning')
#          return redirect(url_for('form'))
#     return render_template('form.html')


def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
    # Обработка данных формы
        name = request.form.get('name')
        flash(f'Привет {name}', 'success')
        return redirect(url_for('form'))

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)


