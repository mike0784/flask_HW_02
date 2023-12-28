from flask import Flask, render_template, request, redirect, url_for
from templates.models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)