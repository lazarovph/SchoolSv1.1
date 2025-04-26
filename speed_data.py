# seed_data.py

from app import create_app, db
from app.models import Course, Level

# Създаваме Flask приложение и активираме контекста
app = create_app()

with app.app_context():
    # Списък с примерни курсове
    courses = [
        Course(name='English A1', description='Beginner English course'),
        Course(name='English B2', description='Upper-Intermediate English course'),
        Course(name='Business English', description='English for business communication'),
    ]

    # Списък с примерни нива
    levels = [
        Level(name='A1', description='Beginner'),
        Level(name='A2', description='Elementary'),
        Level(name='B1', description='Intermediate'),
        Level(name='B2', description='Upper-Intermediate'),
        Level(name='C1', description='Advanced'),
    ]

    # Добавяме ги в базата
    db.session.add_all(courses)
    db.session.add_all(levels)
    db.session.commit()

    print('✅ Курсовете и нивата са добавени успешно!')
