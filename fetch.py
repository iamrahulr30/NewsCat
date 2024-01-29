import feedparser as fp
from datetime import datetime
import pytz
from  uuid import uuid4
from celery_fun import saveToDb , get_content
from models.connection import session 
from models.tables import News
# from main import logger
import logging


def check_contentDB(title):
    news = session.query(News).filter_by(title = title).first()
    if news:
        return True
    return False

def get_data_from_sources(source : list )  :

    """fetched data from give rss fedd links
    
    Keyword arguments:
    source -- contain list of links
    
    """
    

    for link in source:
            print(link)
            hi = fp.parse(link)
            
            if hi.bozo == False :
                for i in hi.entries:
                    try :

                        title = i.title 
                        if check_contentDB(title) == False :
                            uuid = uuid4()
                            article_link = i.link     
                            published = i.published if 'published'  in i else  datetime.now(pytz.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
                        
                            saveToDb.delay(id = uuid, title = title , link = article_link , date = published )
                            get_content.delay(id = uuid  , link = article_link)

                    except Exception as e :
                                logging.exception("Fetch Error")

