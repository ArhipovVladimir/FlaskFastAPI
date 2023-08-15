""""Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact"."""



from flask import Flask

app = Flask(__name__)



@app.route('/about/')
def about():
    return f'Привет, about !'

@app.route('/contact/')
def contact():
    return f'Привет, contact!'


if __name__ == '__main__':
    app.run(debug=True)