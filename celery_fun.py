from celery import Celery
from newspaper import Article
from models.connection import session 
from models.tables import News
from data_models.testing import process
from models.settings import redis_url
import logging as logger


app = Celery('myapp', 
             broker=redis_url, 
             backend=redis_url)


@app.task
def predict(id , content):
    """
    preprocessing the content from get content
    and does prediction and saves pred to DB
    """
    try : 
        label = process(content)
        news = session.query(News).filter_by(id = id).first()
        if news:

            news.label = label
            session.commit()
    except Exception as e :
        logger.exception("Fetch Error")

@app.task
def saveToDb(id , title , link , date):
    """
    saves data  to DB except content
    """
    try :
        doc = News(id = id , title = title , link = link , published_date =  date )
        session.add(doc)
        session.commit()
    except Exception as e :
        logger.exception("Fetch Error")

    
@app.task
def saveContent(id , content):
    """
    saves content fetched using get_content to DB
    """
    
    try :
        news = session.query(News).filter_by(id = id).first()
        if news:
            news.content = content
            session.commit()
    except Exception as e :
        logger.exception("Fetch Error")



@app.task
def get_content(id , link):
    """
        fetched content of article uses newspaper3k module
        Keyword arguments:
        id -- id for DB content storage
        link -- contains url for the page
    """

    try :
        article = Article(link)
        article.download()
        article.parse()
        text = article.text.replace("\n" , " ")
        saveContent.delay(id , text.lower())
        predict.delay(id , text.lower())
    except Exception as e :
        logger.exception("Fetch Error")


# celery -A your-application worker -l info --pool=solo

