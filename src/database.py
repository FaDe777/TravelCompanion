from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv

SQLITE3_DATABASE_URL = getenv("sqlite3_travelcompanion_url")

engine = create_engine(SQLITE3_DATABASE_URL,connect_args={"check_same_thread":False})

