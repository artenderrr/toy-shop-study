import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()
db_url = os.getenv("DB_URL")

if db_url:
    engine = create_engine(db_url)
    Session = sessionmaker(engine.connect())

class Base(DeclarativeBase):
    pass