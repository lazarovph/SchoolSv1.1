from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app as app
from flask_login import login_user, login_required, current_user, logout_user
from app import db, mail
from app.models import User, Task, Solution, Course
from app.auth.forms import LoginForm, RegistrationForm  # Импортираме формите
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer

# Създаване на Blueprint след всички рутове
routes = Blueprint('routes', __name__)

# Генериране на токен за потвърждение
def generate_confirmation_token(email):
    s = Serializer(app.config['SECRET_KEY'], expires_in=3600)  # Токенът изтича след 1 час
    return s.dumps({'email': email}).decode('utf-8')

# Потвърждение на токена
def confirm_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        email = s.loads(token)['email']
    except:
        return False
    return email

@routes.route('/courses')
def courses():
    # Логика за курсовете (например извличане на данни от базата данни)
    courses_list = Course.query.all()  # Ако имате модел Course
    return render_template('courses.html', courses=courses_list)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Създаваме формата за логване
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):  # Проверяваме с криптираната парола
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Login failed. Check username and/or password.', 'danger')

    return render_template('login.html', form=form)  # Предаваме формата към шаблона

@routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Създаваме формата за регистрация
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        role = form.role.data
        password = form.password.data

        # Проверка дали потребителят или имейлът вече съществуват
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('routes.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email is already registered. Please use a different email.', 'danger')
            return redirect(url_for('routes.register'))

        password_hash = generate_password_hash(password)  # Криптиране на паролата

        # Създаваме нов потребител със събраните данни
        new_user = User(username=username, email=email, phone=phone, role=role, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        # Генерираме потвърдителен токен и изпращаме имейл
        token = generate_confirmation_token(email)
        confirm_url = url_for('routes.confirm_email', token=token, _external=True)
        html = f'<p>Натиснете тук, за да потвърдите вашия имейл: <a href="{confirm_url}">Потвърдете имейл</a></p>'
        subject = "Потвърдете имейл адреса си"
        msg = Message(subject, recipients=[email], html=html)
        mail.send(msg)

        flash('Registration successful! Please check your email to confirm.', 'success')
        return redirect(url_for('routes.login'))

    return render_template('register.html', form=form)  # Предаваме формата към шаблона

@routes.route('/confirm_email/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if email:
        user = User.query.filter_by(email=email).first_or_404()
        if user.is_confirmed:
            flash('Email has already been confirmed.', 'info')
        else:
            user.is_confirmed = True  # Потребителят е потвърдил имейла си
            db.session.commit()
            flash('Email confirmed!', 'success')
        return redirect(url_for('routes.login'))
    else:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('routes.index'))

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))
