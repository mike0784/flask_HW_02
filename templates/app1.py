from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
app.config['SECRET_KEY'] = b'0ac75da42726ff2befcb359005d7362cdf46a254951abcc584669946cfd80e31'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()

@app.route('/')
@app.route('/index/')
@csrf.exempt
def index():
    context = {
        'title': "Главная"
    }
    return render_template("index.html", **context)

@app.route('/user/<int:id>/')
def login_user(id):
    context = {
        'title': "Главная",
        'username': 'sdfds',
        'surname': 'dsfsd',
        'name': 'lajnfcs',
        'patronymic': 'fvgdgbvd',
        'email': 'govno@example.com',
        'create_at': '10.10.2023'
    }
    return render_template('user.html', **context)

@app.route('/registration/', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = form.username.data
        surname = form.surname.data
        name = form.name.data
        patronymic = form.patronymic.data
        email = form.email.data
        password = form.password.data
        hash = generate_password_hash(password)
        obj = User(username = user, surname = surname, name = name, patronymic = patronymic, email = email, password = hash)
        db.session.add(obj)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
        
    return render_template('registration.html', form=form)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = form.user.data
        password = form.password.data
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)