import tensorflow as tf
import pickle , string
import spacy , time
from nltk.stem.snowball import SnowballStemmer
from spacy.lang.en.stop_words import STOP_WORDS
import logging

logging.basicConfig(level = logging.DEBUG , filename = "logs_dir/logs.logs" , filemode= "w" ,
                    format="%(asctime)s - %(levelname)s - %(message)s" )


stop_words_set = set(STOP_WORDS)
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
stemmer_ = SnowballStemmer("english")
class_ =  {0: 'natural_disaster', 1: 'others', 2: 'political', 3: 'positive', 4: 'protest', 5: 'terrorism'}



tokenizer = ''
try :
    model = tf.keras.models.load_model("data_models\\model_020_93_065_83_nl.h5")
    with open('data_models\\tokenizer.pkl', 'rb') as handle:
        tokenizer = pickle.load(handle)
except Exception as e :
    logging.exception("Model intialization Error")



def remove_stopwords(text):
    content = []
    for word in text.lower().split():
        if word not in stop_words_set :
            content.append(word)
            
    return " ".join(content)


def stemmer(text):
    doc = nlp(text)
    stemmed_content = [stemmer_.stem(token.lemma_) for token in doc]
    return " ".join(stemmed_content)



def process(text):
    """
    preprocessing stopword elimination stemmer on words tokenize and pad give content and predict class
    
    Keyword arguments:
    text -- str
    Return: class prediction
    """
    
    try :
        translator = str.maketrans('', '', string.punctuation)
        text = stemmer(remove_stopwords(text.translate(translator)))
        tokens = tokenizer.texts_to_sequences([text])
        time.sleep(5)
        pad_seq = tf.keras.preprocessing.sequence.pad_sequences([tokens[0]] , maxlen = 500 ,truncating='post', padding='post')
        pred = model.predict(pad_seq , verbose=0)
    except Exception as e :
        logging.exception("Model intialization Error")
    
    return class_[pred.argmax()]

