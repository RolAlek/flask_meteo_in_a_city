from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
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
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(1, 6)
        ],
    )
    submit = SubmitField("Зарегистрироваться")
