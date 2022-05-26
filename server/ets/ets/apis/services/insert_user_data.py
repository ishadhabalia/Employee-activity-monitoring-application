from dashboard.models import UserBuffer, UserBufferData, UserBufferLocation
import ets.apis.constants as Constants

import pickle

# imports for class scrapTool
from bs4 import BeautifulSoup
import bs4 as bs4
from urllib.parse import urlparse
import requests
from collections import Counter
import pandas as pd
import os

import spacy as sp
from collections import Counter
sp.prefer_gpu()
import en_core_web_sm
nlp = en_core_web_sm.load()
import re

#imports for tokenization
import pandas as pd
import nltk
from nltk.corpus import stopwords as stopWords
# from nltk
from nltk.tokenize import word_tokenize 
import ast
from sklearn.feature_extraction.text import TfidfVectorizer

model = pickle.load(open("./ets/apis/services/wcmodel.sav",'rb'))
fitted_vectorizer=pickle.load(open("./ets/apis/services/fitted_vectorizer.sav",'rb'))


def get_user_buffer_location_data(user_id):
    try:
        user_buffer_location_data = UserBufferLocation.objects.get(user_id=user_id)
        return user_buffer_location_data
    except UserBufferLocation.DoesNotExist:
        return None

def create_user_buffer_location(user_id, data):
    try:
        user_buffer_location_data = UserBufferLocation(user_id=user_id, ip=data.ip, city=data.city, latitude=data.latitude, longitude=data.longitude)
        user_buffer_location_data.save()
    except:
        raise Exception("Location Data could not be intialized")

def update_user_location(instance, data):
    try:
        instance.ip = data.ip
        instance.latitude = data.latitude
        instance.longitude = data.longitude
        instance.city = data.city
        instance.save()
    except:
        raise Exception("Location Data could not be updated")
        

def update_user_location(user_id,data):
    try:
        user_buffer_location_data = get_user_buffer_location_data(user_id)
        if user_buffer_location_data is None:
            create_user_buffer_location(user_id,data)
        else:
            update_user_location(user_buffer_location_data, data)
            return True
    except:
        return False
        

import json
from rest_framework.decorators import api_view

def insert_user_activity(user_id,data):
    # if data.keys() != Constants.ACTIVITY_DATA.keys():
    #     raise Exception("Wrong data format")
    try:
        print(data)
        print(type(data))
        data = json.loads(data)
        
        from datetime import datetime
        data["date"] = datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")

        # prodVal = predictProductivity(str(['emp-tracking','vscode']))
        prodVal = predictProductivity(str(data["process"]))
        print(prodVal)
        # user_activity_data = UserBufferData(id='1',user_id=obj,process_name=data["process"],date=data["date"], productive=prodVal, created_on=data["date"], updated_on=data["date"])
        obj = UserBuffer.objects.first()
        post = UserBufferData()
        # post.id = 2
        post.user_id = obj
        post.created_on = data["date"]
        post.updated_on = data["date"]
        post.productive = prodVal
        post.date = data["date"]
        post.process_name = data["process"]
        post.save()
    except:
        print("exception")
        return False



'''
Below functions and classes are for the purpose of classification of user activity as productive/unproductive
'''

def predictProductivity(processName):
    
    #
    scrapTool = ScrapTool()
    stop_words = set(stopWords.words('english')) 
    vectorizer1 = TfidfVectorizer()
    vectorizer2 = TfidfVectorizer()
    # rows=len(df.index)
    id_to_category={0: 'Travel', 1: 'Social Networking and Messaging', 2: 'News', 3: 'Streaming Services', 4: 'Sports', 
    5: 'Photography', 6: 'Law and Government', 7: 'Health and Fitness', 8: 'Games', 9: 'E-Commerce', 10: 'Forums', 11: 'Food', 12: 'Education', 13: 'Computers and Technology', 14: 'Business/Corporate', 15: 'Adult'}
    productive_list=['Education','Computers and Technology','Business/Corporate']

    lst=str(processName)
    lst = ast.literal_eval(lst)
    question = filter_str(str(lst[-1]))

    
    if(question=="Google Chrome"):
        
        question2 = filter_str(str(lst[0]))
        genre=get_genre(question2)
        question=question+"->"+question2
    else:
        genre=get_genre(question, scrapTool, fitted_vectorizer, model, id_to_category )

    category=get_category(genre,productive_list)
    print(category)
    convDict = {"productive":1, "unproductive":0}
    return convDict[category]



class ScrapTool:
    def visit_url(self, website_url):
        '''
        Visit URL. Download the Content. Initialize the beautifulsoup object. Call parsing methods. Return Series object.
        '''
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        content = requests.get(website_url,timeout=60).content
        
        #lxml is apparently faster than other settings.
        soup = BeautifulSoup(content, "html5lib")
        result = {
            "website_url": website_url,
            "website_name": self.get_website_name(website_url),
            "website_text": self.get_html_title_tag(soup)+self.get_html_meta_tags(soup)+self.get_html_heading_tags(soup)+
                                                            self.get_text_content(soup)
        }
        
        #Convert to Series object and return
        return pd.Series(result)
    
    def get_website_name(self,website_url):
        '''
        Example: returns "google" from "www.google.com"
        '''
        return "".join(urlparse(website_url).netloc.split(".")[-2])
    
    def get_html_title_tag(self,soup):
        '''Return the text content of <title> tag from a webpage'''
        return '. '.join(soup.title.contents)
    
    def get_html_meta_tags(self,soup):
        '''Returns the text content of <meta> tags related to keywords and description from a webpage'''
        tags = soup.find_all(lambda tag: (tag.name=="meta") & (tag.has_attr('name') & (tag.has_attr('content'))))
        content = [str(tag["content"]) for tag in tags if tag["name"] in ['keywords','description']]
        return ' '.join(content)
    
    def get_html_heading_tags(self,soup):
        '''returns the text content of heading tags. The assumption is that headings might contain relatively important text.'''
        tags = soup.find_all(["h1","h2","h3","h4","h5","h6"])
        content = [" ".join(tag.stripped_strings) for tag in tags]
        return ' '.join(content)
    
    def get_text_content(self,soup):
        '''returns the text content of the whole page with some exception to tags. See tags_to_ignore.'''
        tags_to_ignore = ['style', 'script', 'head', 'title', 'meta', '[document]',"h1","h2","h3","h4","h5","h6","noscript"]
        tags = soup.find_all(text=True)
        result = []
        for tag in tags:
            stripped_tag = tag.strip()
            if tag.parent.name not in tags_to_ignore\
                and isinstance(tag, bs4.element.Comment)==False\
                and not stripped_tag.isnumeric()\
                and len(stripped_tag)>0:
                result.append(stripped_tag)
        return ' '.join(result)


def clean_text(doc):
    '''
    Clean the document. Remove pronouns, stopwords, lemmatize the words and lowercase them
    '''
    doc = nlp(doc)
    tokens = []
    exclusion_list = ["nan"]
    for token in doc:
        if token.is_stop or token.is_punct or token.text.isnumeric() or (token.text.isalnum()==False) or token.text in exclusion_list :
            continue
        token = str(token.lemma_.lower().strip())
        tokens.append(token)
    return " ".join(tokens) 
    
def filter_str(text):
  global stop_words
  word_tokens = word_tokenize(text) 
  """making tokens """
  stoplist = set(stopWords.words("english"))
  filtered_sentence = [w for w in word_tokens if not w in stoplist]
  filtered_sentence=[i.split('\\')[-1] for i in filtered_sentence ]
  return " ".join(filtered_sentence)

# function parameters
def get_genre(question, scrapTool, fitted_vectorizer, model, id_to_category):
  website='https://www.google.com/search?channel=fs&client=ubuntu&q='+question
  web=dict(scrapTool.visit_url(website))
  text=(clean_text(web['website_text']))
  t=fitted_vectorizer.transform([text])
  genre=id_to_category[model.predict(t)[0]]
  return genre

# parameters
def get_category(genre, productive_list):
    category="unproductive"
    for i in range(len(productive_list)):
        if(genre==productive_list[i]):
            category="productive"    
    return category