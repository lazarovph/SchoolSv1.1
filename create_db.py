# create_db.py
from app import create_app, db

app = create_app()

# Създаване на базата данни
with app.app_context():
    db.create_all()
