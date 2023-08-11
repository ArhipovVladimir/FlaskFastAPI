from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Владимир',
    }
    return render_template('index.html', **context)

@app.route('/if/')
def show_if():
    context = {
        'title': 'Личный блог',
        'user': 'Владимир',
        'number': 15
    }
    return render_template('show_if.html', **context)

@app.route('/for/')
def show_for():

         context = {'poem': ['Вот не думал, не гадал,',
                            'Программистом взял и стал.',
                            'Хитрый знает он язык,',
                            'Он к другому не привык.']}

         return render_template('show_for.html', **context)

@app.route('/users/')
def users():
        _users = [{'name': 'Никанор',
            'mail': 'nik@mail.ru',
            'phone': '+7-987-654-32-10',
            },
            {'name': 'Феофан',
            'mail': 'feo@mail.ru',
            'phone': '+7-987-444-33-22',
            },
            {'name': 'Оверран',
            'mail': 'forest@mail.ru',
            'phone': '+7-903-333-33-33',
            }]

        context = {'users': _users,
                   'title': 'Точечная нотация'}

        return render_template('process.html', **context)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('new_main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('new_data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

