from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from . import app, db
from app.forms import UserRegisterForm
from app.models import User

@app.route("/")
def get_weather():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        hash_pass = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            password=hash_pass,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass
