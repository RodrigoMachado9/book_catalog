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

    return render_template('movies.html', movies=movie_list, name='Rodrigo')


if __name__ == '__main__':
    app.run(debug=True)
