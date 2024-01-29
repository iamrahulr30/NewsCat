from fetch import get_data_from_sources
from models.connection import session
from models.tables import News
import logging
import json

logging.basicConfig(level = logging.DEBUG , filename = "logs_dir/logs.logs" , filemode= "w" ,
                    format="%(asctime)s - %(levelname)s - %(message)s" )


feed_urls = ["http://rss.cnn.com/rss/cnn_topstories.rss", 
             "http://qz.com/feed", 
             "http://feeds.foxnews.com/foxnews/politics", 
             "http://feeds.feedburner.com/NewshourWorld", 
             "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml",
]

def export_json(file_name):
    """
    fetched data from DB returns jsonfile
    """
    
    rows = session.query(News).all()
    with open(f'output/{file_name}.json', 'w') as json_file:
        json.dump([row.__dict__ for row in rows], json_file, default=str, indent=2)

if __name__ == "__main__" :
    logging.info("Fetching data")
    get_data_from_sources(feed_urls)
    export_json("out")

    

