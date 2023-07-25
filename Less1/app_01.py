from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def index(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/number/<float:num>/')
def set_numder(num):
    print(type(num))
    return f'передано число "{num}"'


@app.route('/file/<path:file>')
def set_path(file):
    print(type(file))
    return f'путь до файла "{file}"'


html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():

    poem = ['Вот не думал, не гадал,',
    'Программистом взял и стал.',
    'Хитрый знает он язык,',
    'Он к другому не привык.',]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) +'</p>'

    return txt



@app.route('/Николай/')
def nike():
    return 'Привет Николай!'

@app.route('/Иван/')
def ivan():
    return 'Привет Ванечка!'

@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет Федька!'

if __name__ == '__main__':
    app.run(debug=True)