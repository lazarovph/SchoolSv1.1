# app/models/solution.py
from app import db

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    task = db.relationship('Task', backref=db.backref('solutions', lazy=True))

    def __repr__(self):
        return f'<Solution {self.id}>'
