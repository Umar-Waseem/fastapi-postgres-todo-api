# database.py
# Description: contains the database schema and the database connection for SQLAlchemy ORM for python

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
dbname = os.environ.get("DBNAME")
host = os.environ.get("HOST")

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)