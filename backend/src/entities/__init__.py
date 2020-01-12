from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_conn_str = 'sqlite:///data.db'

engine = create_engine(db_conn_str)

Session = sessionmaker(bind=engine)

Base = declarative_base()