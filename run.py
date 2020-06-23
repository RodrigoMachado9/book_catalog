from flask import Flask, request, render_template

app = Flask(__name__)


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
                           name=None,
                           film='a new day machado')


if __name__ == '__main__':
    app.run(debug=True)
