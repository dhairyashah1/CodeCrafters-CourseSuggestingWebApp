from coursespot import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True) 
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True) 
    message = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"Contact('{self.email}', '{self.message}')"