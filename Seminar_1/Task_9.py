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
@app.route('/coloting/')
def coloting():

    shurc=[Object('Зима', 'Cиний', 42), Object('Лето', 'Красный', 42), Object('Осень', 'Желтый', 42)]
    return render_template('Сoloting.html', shurc=shurc)

@app.route('/shoes/')
def shoes():

    shoes=[Object('Зима', 'Бордо', 43), Object('Лето', 'Фиалка', 43), Object('Осень', 'Голубой', 43)]
    return render_template('Сoloting.html', shurc=shoes)

@app.route('/jacket/')
def jacket():

    jacket=[Object('Зима', 'Черный', 44), Object('Лето', 'Коричневый', 44), Object('Осень', 'Белый', 44)]
    return render_template('Сoloting.html', shurc=jacket)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
