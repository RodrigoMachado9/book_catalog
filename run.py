from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
    SECRET_KEY='postgres',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATION=False)

db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def index():
    return "<body><h1>x</h1><h2>y</h2><h3>z</h3></body>"


@app.route('/new')
def query_string():
    query = request.args.get("greeting")
    payload = request.json
    if payload:
        return "<h1>the greeting is : {0}</h1><h2>{1}</h2>".format(query, payload)
    return "<h1>the greeting is : {0}</h1>".format(query)


@app.route('/demo/string/<string:name>')
def route_by_string(name):
    return "hello {0}".format(name)


@app.route('/template')
def rendering_template():
    return render_template('index.html')


@app.route('/watch')
def demo_jinja2_template():
    movie_list = ['autopsy of jane done',
                  'neon demon',
                  'ghost  in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html', movies=movie_list, name='rodrigo')


@app.route('/tables')
def demo_jinja2_of_dict():
    movies_dict = {
        'autopsy of jane done': 02.14,
        'neon demon': 3.20,
        'ghost  in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2': 02.52,
        'spiderman - homecoming': 1.48
    }
    return render_template('table_data.html',
                           movies=movies_dict,
                           name='rmachado')


@app.route('/filters')
def filter_data():
    movies_dict = {
        'autopsy of jane done': 02.14,
        'neon demon': 3.20,
        'ghost  in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2': 02.52,
        'spiderman - homecoming': 1.48
    }
    return render_template('filter_data.html',
                           movies=movies_dict,
                           name="machado",
                           film='a new day machado')


@app.route('/macros')
def jinja2_macros():
    movies_dict = {
        'autopsy of jane done': 02.14,
        'neon demon': 3.20,
        'ghost  in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2': 02.52,
        'spiderman - homecoming': 1.48
    }
    return render_template('using_macros.html', movies=movies_dict)


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "The name is {}".format(self.name)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    book_format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # relationship > book 1 ------ 1 publication
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.book_format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
