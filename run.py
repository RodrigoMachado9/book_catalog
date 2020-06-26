from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc


flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='rodrigo').first():
            User.create_user(user='rodrigo', email='rodrigo.machado3.14@hotmail.com', password='secret666')
    except exc.IntegrityError:
        flask_app.run()


# if __name__ == '__main__':
#     flask_app = create_app('dev')
#     with flask_app.app_context():
#         db.create_all()
#         if not User.query.filter_by(user_name='rodrigo').first():
#             User.create_user(user='rodrigo', email='rodrigo.machado3.14@hotmail.com', password='secret666')
#     flask_app.run(debug=True)