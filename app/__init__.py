from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# Инициализация на базата данни и Mail
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    
    # Конфигурация на приложението
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Променете на вашия URI за базата данни
    app.config['SECRET_KEY'] = 'your_secret_key'  # Задайте таен ключ
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Примерен mail server
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
    app.config['MAIL_PASSWORD'] = 'your_email_password'

    # Инициализация на db и mail
    db.init_app(app)
    mail.init_app(app)

    from app.routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
