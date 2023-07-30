from pathlib import PurePath, Path
from flask import Flask, request, render_template, url_for, abort, redirect, flash, make_response, session
from werkzeug.utils import secure_filename
import logging
from db import get_blog

logger = logging.getLogger(__name__)

app = Flask(__name__)

# @app.route('/<path:file>/')
# def get_file(file):
#     return f'Ваш файл находится в: {escape(file)}!'



@app.route('/test_url_for/<int:num>/')
def test_url(num):
        text = f'В num лежит {num}<br>'
        text += f'Функция {url_for("test_url", num=42) = }<br>'
        text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
        text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
        return text

# @app.route('/about/')
# def about():
#
#     context = {'title': 'Обо мне',
#                'name': 'Архипов'}
#     return render_template('base.html', **context)

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}!'
#     return render_template('form.html')

@app.get('/submit/')
def submit_get():
    return render_template('form.html')
@app.post('/submit/')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'




@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('new_main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('new_data.html', **context)
@app.route('/uploads/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('uploads.html')

# @app.route('/')
# def index():
#     return '<h1>Hello world!</h1>'

# @app.errorhandler(404)
# def page_not_found(e):
#     app.logger.warning(e)
#     context = {'title': 'Страница не найдена',
#                 'url': request.base_url,
#                }
#     return render_template('404.html', **context), 404

# @app.route('/blog/<int:id>')
# def get_blog_by_id(id):
# # делаем запрос в БД для поиска статьи по id
#     result = get_blog(id)
#     if result is None:
#         abort(404)

# возвращаем найденную в БД статью
# @app.errorhandler(404)
# def page_not_found(e):
#     logger.warning(e)
#     context = {'title': 'Страница не найдена',
#                 'url': request.base_url}

    return render_template('404.html', **context), 404

@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
        }
    return render_template('500.html', **context), 500
@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))

@app.route('/external')
def external_redirect():
    return redirect('https://google.com')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))

app.secret_key = '62e14179dd8dea918d1375fd65876e8568034827b5bee3a9f037ae36e3922ec4'

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#     # Обработка данных формы
#         flash('Форма успешно отправлена!', 'success')
#         return redirect(url_for('form'))
#     return render_template('form.html')

"""
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
    # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))

    return render_template('form.html')


# @app.route('/')
# def index():
#         #  устанавливаем cookie
#         response = make_response("Cookie установлен")
#         response.set_cookie('username', 'admin')
#         return response
@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
        name = request.cookies.get('username')
        return f"Значение cookie: {name}"

# @app.route('/')
# def index():
#
#     context = {
#         'title': 'Главная',
#         'name': 'Владимир'}
#     response = make_response(render_template('main_1.html', **context))
#     response.headers['new_head'] = 'New value'
#     response.set_cookie('username', context['name'])
#     return response

@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port = 5000, debug=True)
    # app.run(debug=False)

