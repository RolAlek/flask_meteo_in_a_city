# Flask weather web-app
Небольшой вэб-сервис для проверки погоды на ближайшее время в интересующем городе, отлично подойдет тем кто отправляется в путешествие или командировку

## Стэк:
* Python 3.12
* Poetry
* Docker + Docker Compose
* Flask 3.0.3
    + Flask-Form
    + Flask-Login
* Дополнительно:
    + opencage для получения координат города
    + GeoName для автокомплита

Для работы нужно только:
* В корне проекта создать .env-файлик как в .env.example:
    ```
    FLASK_APP=app
    FLASK_DEBUG=1

    SECRET=MY SECRET KEY

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=weather_db

    GEOCODE_KEY=зарегистрируйтесь на https://opencagedata.com/ для получения ключа
    GEONAME=https://www.geonames.org/ - регистрируйся для работы автокомплита
    ```

* запустить сервис выполнив
    ```sh
    docker compose up
    ```
* перейти по адресу http://localhost:5001

<details>
<summary>
Для разработчиков:
</summary>
Если вы хотите внести необходимые вам изменения и доработки, то после клонирования репозитория:
* создайте .env в корне проекта как .env.exmple
* установите менеджер зависимостей Poetry

```sh
pip install poetry
```

* примените зависимости

```sh
poetry install
```

* примените миграции

```sh
flask db upgrade
```

* запустите сервер

```sh
flask run
```
</details>


>[!NOTE]
> если желаешь хранить историю запросов то для вас есть возможность зарегистрироваться в проекте(кнопки "зарегистрироваться" и "войти")

>[!NOTE]
> есть очень удобный автокомплит городов - просто начни вводить город и магия случится.