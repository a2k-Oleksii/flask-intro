from app import app
from flask import render_template


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/keklol')
def keklol():
    return 'Hello Keklol'


@app.route('/hello/<string:name>/<string:last_name>')
def hello_user(name, last_name):
    return render_template("index.html", name=name, last_name=last_name)


@app.route('/calc/<int:first_int>/<int:second_int>')
def calc(first_int, second_int):
    return render_template("index.html", first_int=first_int, second_int=second_int, result=first_int+second_int)


#@app.route('/news/<int:id>')
#def news(id):
#    return news
