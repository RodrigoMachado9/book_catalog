# app/__init__.py
from datetime import datetime
from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now)

    # class method  belong to a class but are not associated with any class instance
    @classmethod
    def create_user(cls, user, email, password):
        user = cls(
            user_name=user,
            user_email=email,
            user_password=bcrypt.generate_password_hash(password).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        return user
