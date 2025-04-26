from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Създаване на обектите за база данни, миграции и потребителско влизане
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Това зарежда config.py

    # Инициализиране на db, migrate и login_manager с app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Регистриране на blueprint-а за маршрути (routes)
    from app.routes import routes
    app.register_blueprint(routes)

    # Връщане на конфигурираното приложение
    return app
