from .settings import Settings
import sqlalchemy
from sqlalchemy.orm import sessionmaker


DB_URL = Settings().DB_URL

engine = sqlalchemy.create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
