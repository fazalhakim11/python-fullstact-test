import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://admin:admin@localhost:5432/mydatabase")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
