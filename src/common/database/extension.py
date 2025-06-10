import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setting import settings
from src.common.property import prop

SQLALCHEMY_DATABASE_URL = prop.get("SQLALCHEMY_DATABASE_URL")
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_recycle=3600,
    pool_pre_ping=True,
    # connect_args={"disable_oob": True, "expire_time": 600},
)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

redis_client = redis.Redis(
    host=prop.get("REDIS_URL"), port=prop.get("REDIS_PORT"), db=prop.get("REDIS_DB")
)
