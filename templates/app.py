from flask import Flask
from flask import render_template
from flask import request, make_response, redirect, url_for

app = Flask(__name__)

title = ['user', 'email', 'action']

@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': "temp",
        title[2]: "/hello/"
    }
    return render_template("index.html", **context)
    
@app.post('/hello/')
def submit_post():
    user = request.form.get(title[0])
    email = request.form.get(title[1])
    context = {
        'title': 'Приветствие',
        title[0]: user,
        title[1]: email,
        title[2]: '/logout/'
    }    
    response = make_response(render_template('hello.html', **context))
    response.set_cookie(title[0], user)
    response.set_cookie(title[1], email)

    return response

@app.get('/logout/')
def submit_get():
    response = make_response(redirect(url_for('index')))
    response.set_cookie(title[0], "aa", max_age = 0)
    response.set_cookie(title[1], "bb", max_age = 0)
    return response

if __name__ == '__main__':
    app.run(debug=True)