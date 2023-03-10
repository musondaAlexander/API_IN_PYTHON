#  we will write basic database operations in python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# setting up the connection to the database string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:flames####@localhost/fastApiDb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# create a depe
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()