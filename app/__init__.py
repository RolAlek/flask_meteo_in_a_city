from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.settings import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def weather_view():
    return "Скоро тут вы сможете посмотреть погоду в выбранном городе!"


if __name__ == "__main__":
    app.run()
