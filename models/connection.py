from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists , create_database
from models.settings import postgres_url

 


engine = create_engine(postgres_url)
session = sessionmaker(bind = engine)
session = session()
