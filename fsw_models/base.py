from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config

Base = declarative_base()
if config.DB_TYPE == "MySQL":
    engine = create_engine(config.MYSQL_DB_URI)
else:
    engine = create_engine(config.SQLITE_DB_URI)
DatabaseSession = sessionmaker(bind = engine)