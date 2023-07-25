"""Задание №9
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('base.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


class Object:
    def __init__(self, model, color, sise):
        self.model = model
        self.color = color
        self.size = sise

@app.route('/jacket/')
def jacket():

    _jacket=[Object('Зима', 'Черный', 44),]

    context = {'shurc': _jacket,
               'title': 'Куртки',
               'number': len(_jacket)}

    return render_template('shurc.html', **context)

@app.route('/coloting/')
def coloting():

    _shurc=[Object('Зима', 'Cиний', 41), Object('Лето', 'Красный', 42), Object('Осень', 'Желтый', 42), Object('Осень', 'Желтый', 42), Object('Осень', 'Желтый', 42)]

    context = {'shurc': _shurc,
               'title': 'Одежда',
               'number': len(_shurc)}

    return render_template('shurc.html', **context)

@app.route('/shoes/')
def shoes():

    _shoes=[Object('Зима', 'Бордо', 41), Object('Лето', 'Фиалка', 43), Object('Осень', 'Голубой', 43)]

    context = {'shurc': _shoes,
               'title': 'Обувь',
               'number': len(_shoes)}

    return render_template('shurc.html', **context)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
