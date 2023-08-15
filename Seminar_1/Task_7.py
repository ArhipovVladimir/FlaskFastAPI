"""Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст."""

from flask import Flask
from flask import render_template

app = Flask(__name__)

class News:
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date
@app.route('/')
def news():
    news = [News('Какая то новость', 'Описание','23-06-1981'), News('Какая то новость', 'Описание','23-06-1981'), News('Какая то новость', 'Описание','23-06-1981'), News('Какая то новость', 'Описание','23-06-1981'), News('Какая то новость', 'Описание','23-06-1981')]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)

