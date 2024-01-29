from models.connection import session , engine
from sqlalchemy import Column , String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import UUIDType
import datetime
from uuid import uuid4

Base = declarative_base()


class News(Base):
    """
    storing fetched articles
    label : stores model classification 

    """
    
    __tablename__ = 'news'

    id = Column(UUIDType(binary=False), primary_key=True, default= uuid4 )
    title = Column(String , nullable=False )
    content = Column(String)
    link = Column(String)
    label = Column(String)
    published_date = Column(DateTime, default=datetime.datetime.utcnow , nullable=False )

    def __repr__(self):
        return f"<News(title='{self.title}', published_date='{self.title[:10]}' , published_date='{self.published_date}')>"



Base.metadata.create_all(engine) # table creation