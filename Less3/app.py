from flask import Flask, render_template, jsonify, request
from model import db, User, Post, Comment
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect
from form import LoginForm, RegistrationForm

from flask_wtf import FlaskForm


app3 = Flask(__name__)
app3.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app3)
app3.config['SECRET_KEY'] = b'6839b6fed8acf1fdb2ebf7e0cd1847f2db13de12ae2ca2467694c477824b3cec'
csrf = CSRFProtect(app3)

"""
import secrets
secrets.token_hex()
"""


@app3.route("/")
def index():
    return 'Hi'


@app3.cli.command("init-db")
# @app.route("/init")
def init_db():
    db.create_all()
    return 'OK'
    print('OK')


@app3.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()


    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


@app3.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('process.html', **context)


@app3.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('process.html', **context)


@app3.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title,
                         'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


@app3.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
            return jsonify([{'id': post.id, 'title': post.title,
                             'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

@app3.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app3.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('process.html', form=form)



if __name__ == '__main__':
    app3.run(debug=True)

