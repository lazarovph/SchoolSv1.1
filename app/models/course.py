from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)

    level = db.relationship('Level', backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return f"<Course {self.name}>"
