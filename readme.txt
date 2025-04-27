git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/lazarovph/SchoolSv1.1.git
git push -u origin main

from app import create_app, db
app = create_app()
with app.app_context():
db.create_all()

