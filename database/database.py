from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:P%40ssword1!@localhost/StudentsDB"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    print(SQLALCHEMY_DATABASE_URL)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
