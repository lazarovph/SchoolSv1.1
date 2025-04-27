from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Инициализация на базата данни
db = SQLAlchemy()

# Инициализация на LoginManager
login_manager = LoginManager()
login_manager.login_view = "routes.login"  # Пренасочване към login, ако потребителят не е влязъл

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'your_secret_key'  # Променете това на истински ключ за продукция

    db.init_app(app)
    login_manager.init_app(app)  # Инициализиране на LoginManager

    from app.routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app

# Зареждаме потребителя по неговия ID
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
