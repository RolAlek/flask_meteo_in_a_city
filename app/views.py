from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.forms import ChoiceCityForm, UserLoginForm, UserRegisterForm
from app.models import User
from app.utils import get_coordinates, get_weather_data, save_search

from . import app, db

load_dotenv()


@app.route("/", methods=["GET", "POST"])
def get_weather():
    weather_data = None
    form = ChoiceCityForm()
    city = None

    if request.method == "POST":
        if form.validate_on_submit():
            city = form.city.data
    else:
        city = request.args.get("city")

    if city:
        coordinates = get_coordinates(city)
        if coordinates:
            weather_data = get_weather_data(coordinates)
            if current_user.is_authenticated:
                save_search(city, current_user.id)
        else:
            flash("Город не найден", "error")
        history = (
            current_user.searches
            if current_user.is_authenticated
            else None
        )
        weather_data["city"] = city
        return render_template(
            "index.html",
            form=form,
            weather=weather_data,
            history=history,
        )
    return render_template("index.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()

    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash("Пользователь с таким e-mail уже существует", "error")
            return redirect(url_for("register"))

        hash_pass = generate_password_hash(form.password.data)
        user = User(
            email=form.email.data,
            password=hash_pass,
        )
        db.session.add(user)
        db.session.commit()
        flash("Вы успешно зарегистрировались", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("get_weather"))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not check_password_hash(
            user.password,
            form.password.data,
        ):
            flash("Неверный логин или пароль", "error")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("get_weather"))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_weather"))
