from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    EmailField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, Length


class UserRegisterForm(FlaskForm):
    email = EmailField(
        "Введите email",
        validators=[
            DataRequired(message="Обязательное поле"),
            Email(),
        ],
    )
    password = PasswordField(
        "Введите пароль",
        validators=[DataRequired(message="Обязательное поле"), Length(min=6)],
    )
    submit = SubmitField("Зарегистрироваться")


class UserLoginForm(UserRegisterForm):
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class ChoiceCityForm(FlaskForm):
    city = StringField(
        "Выберите город",
        validators=[DataRequired("Обязательное поле")],
    )
    submit = SubmitField("Получить погоду")
