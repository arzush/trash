from config import Config
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, flash, render_template, request
from app import db
from app.forms import LoginForm
from flask_login import login_user
app = Flask(__name__)
app.config.from_object(Config)

#db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI']
#db.init_app(app)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('normative'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('normative'))
    # if request.method == 'POST':
    #     # Обработка запроса на регистрацию
    #     if 'register' in request.form:
    #         username = request.form.get('username')
    #         email = request.form.get('email')
    #         password = request.form.get('password')
    #
    #         # Проверка, что пользователь с таким именем или электронной почтой уже не зарегистрирован
    #         existing_user = User.query.filter_by(username=username).first()
    #         if existing_user:
    #             return 'Username already exists'
    #
    #         existing_email = User.query.filter_by(email=email).first()
    #         if existing_email:
    #             return 'Email already exists'
    #
    #         # Создание нового пользователя и сохранение его в базе данных
    #         new_user = User(username, email, password)
    #         db.session.add(new_user)
    #         db.session.commit()
    #
    #         return 'User registered successfully'
    #
    #     # Обработка запроса на вход
    #     elif 'login' in request.form:
    #         username = request.form.get('username')
    #         password = request.form.get('password')
    #
    #         # Поиск пользователя в базе данных
    #         user = User.query.filter_by(username=username).first()
    #         if user:
    #             # Проверка пароля
    #             if user.check_password(password):
    #                 # Выполнение действий для успешного входа
    #                 return 'Logged in successfully'
    #             else:
    #                 return 'Incorrect password'
    #         else:
    #             return 'User not found'
    #
    #     # Отображение страницы с формой входа и регистрации
    # #return render_template('login.html')
    # return render_template('loginform.html', title='Sign In')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Получить данные из формы
        fullname = request.form['fullname']
        email = request.form['name']
        password = request.form['password']

        # Создать нового пользователя
        new_user = User(username=fullname, email=email)
        new_user.set_password(password)

        # Добавить пользователя в базу данных
        db.session.add(new_user)
        db.session.commit()

        return 'Регистрация успешно завершена.'

    # Отобразить форму регистрации
    return render_template('registerform.html')

@app.route('/normative')
def normative():
    return render_template('formnormative.html')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
