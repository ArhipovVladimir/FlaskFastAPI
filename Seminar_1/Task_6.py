"""
Задание №6
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""
from flask import Flask
from  flask import render_template

app = Flask(__name__)

_student = [{'firstname': 'Никанор',
             'lastname': 'Федоров',
             'age': 23,
             'rate': 20,
             },
            {'firstname': 'Степан',
             'lastname': 'Иванов',
             'age': 22,
             'rate': 33,
             },
            {'firstname': 'Федор',
             'lastname': 'Петров',
             'age': 17,
             'rate': 40,
             },]
@app.route('/students/')
def users():


        context = {'students': _student,
                   'title': 'Таблица студентов'}

        return render_template('student.html', **context)

if __name__ == '__main__':
    app.run(debug=True)