"""
Задание №1
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.

"""
from random import randint, choice
from flask import Flask, render_template
from Task_1.model import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db.init_app(app)


@app.route("/")
def index():
    return 'Hello'


@app.cli.command("cre-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-stud")
def fill_tables():
    for i in range(5):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)
    db.session.commit()
    print('OK1')

    for i in range(20):
        student = Student(
           name=f'name {i}', surname=f'surname {i}', age=20, sex=True, group=f'group_{i}', faculty_id=randint(0, 4))
        db.session.add(student)
    db.session.commit()
    print('OK2')


@app.route('/students/')
def all_students():
    students = Student.query.all()
    print(type(students))
    print('OKclearKK')
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)





