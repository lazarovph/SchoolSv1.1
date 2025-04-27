from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from app import db
from app.models import User, Task, Solution, Course
from app.auth.forms import LoginForm, RegistrationForm  # Импортираме формите
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import User
from flask_login import login_user, login_required

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def index():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Успешно влезе!', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Грешка при вход. Проверете потребителското име и парола.', 'danger')

    return render_template('login.html')

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Успешна регистрация!', 'success')
        return redirect(url_for('routes.login'))

    return render_template('register.html')

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def index():
    return render_template('index.html')

@routes.route('/courses')
@login_required
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@routes.route('/levels')
@login_required
def levels():
    return render_template('levels.html')

@routes.route('/tasks')
@login_required
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@routes.route('/task/<int:task_id>')
@login_required
def task(task_id):
    task = Task.query.get_or_404(task_id)
    solutions = Solution.query.filter_by(task_id=task.id).all()
    return render_template('task_detail.html', task=task, solutions=solutions)

@routes.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    if current_user.role != 'teacher':
        flash('You are not authorized to create tasks', 'danger')
        return redirect(url_for('routes.index'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']

        task = Task(title=title, description=description, due_date=due_date, created_by=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully', 'success')
        return redirect(url_for('routes.tasks'))

    return render_template('create_task.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Създаваме формата за логване
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Login failed. Check username and/or password.', 'danger')

    return render_template('login.html', form=form)  # Предаваме формата към шаблона

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))
