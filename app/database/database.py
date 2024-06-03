from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_url():
    return "sqlite:///./sql_app.db"

engine = create_engine(get_url(), connect_args={})

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

def create_tables():
	Base.metadata.create_all(bind=engine)
     
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
