import os
import sys

from dotenv import load_dotenv

APP_ENV = sys.argv[1]

# gunicorn으로 실행 될 경우
if APP_ENV == "main:app":
    APP_ENV = os.getenv("ENVIRONMENT", "dev")

if APP_ENV == "local":  # 로컬
    load_dotenv("src/resources/config/local/.env")
    load_dotenv("src/resources/config/local/db.env")


def get(key):
    return os.environ[key]


def is_local() -> bool:
    return os.environ["environment"] == "local"
