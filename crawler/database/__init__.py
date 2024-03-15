import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

DATABASE_AT_BAY_URL = os.environ.get('DATABASE_URL')

if not DATABASE_AT_BAY_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_AT_BAY_URL)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
