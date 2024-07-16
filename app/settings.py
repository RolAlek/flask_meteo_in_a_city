import os


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:'
        f'{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/'
        f'{os.getenv('POSTGRES_DB')}'
    )
