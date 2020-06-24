from app import create_app, db

if __name__ == '__main__':
    flask_app = create_app('dev')

    # http://flask-sqlalchemy.pocoo.org/2.3/contexts/
    with flask_app.app_context():
        db.create_all()
    flask_app.run(debug=True)


