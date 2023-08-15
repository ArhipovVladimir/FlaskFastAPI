"""
Задание №5
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/first/')
def show_():
    context = {
        'title': 'Моя первая HTML страница',
        'print': 'Привет Мир'
    }

    return render_template('Task5.html', **context)





if __name__ == '__main__':
    app.run(debug=True)