FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /

RUN pip install --no-cache-dir poetry==1.8.2 && poetry config virtualenvs.create false && poetry install

COPY . .

RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD flask run --host=0.0.0.0
