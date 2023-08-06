"""
Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

"""

from flask import Flask, request, render_template, redirect, url_for, abort, flash, make_response, session

app_hw = Flask(__name__)

app_hw.secret_key = '62e14179dd8dea918d1375fd65876e8568034827b5bee3a9f037ae36e3922ec4'


@app_hw.route('/', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['mail'] = request.form.get('mail')
        print(session)
        return render_template('info.html', name=session['username'])
    return render_template('account.html')

@app_hw.route('/logout/')
def logout():
        session.pop('username', None)
        session.pop('mail', None)
        print(session)
        return redirect(url_for('account'))


# @app_hw.route('/info/')
# def info():
#     return redirect(url_for('account'))


if __name__ == '__main__':
    app_hw.run(debug=True)
