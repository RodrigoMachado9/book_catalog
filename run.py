from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')

    # http://flask-sqlalchemy.pocoo.org/2.3/contexts/
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='rodrigo').first():
            User.create_user(
                user='rodrigo',
                email='rodrigo.machado3.14@hotmail.com',
                password='secret666'
            )
    flask_app.run(debug=True)

