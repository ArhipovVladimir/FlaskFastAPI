from flask import Flask
from  flask import render_template

app = Flask(__name__)

@app.route('/if/')
def show_if():
    context = {
        'title': 'Личный блог',
        'user': 'Владимир',
        'number': 15
    }
    return render_template('show_if.html', **context)


@app.route('/')
@app.route('/<name>/')
def index(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'



if __name__ == '__main__':
    app.run(debug=True)

