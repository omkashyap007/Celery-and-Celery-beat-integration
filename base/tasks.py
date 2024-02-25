import random
import requests
from celery import shared_task
from datetime import datetime
from data import (
    NEWS_API_ORG_API_KEY ,
    NEWS_API_TOP_HEADLINES_GET_REQUEST ,
    NEWS_API_EVERYTHING_GET_REQUEST
)
from base.models import News

hash_map = {}
@shared_task(bind = True)
def updateCount(self , user_id) :
    hash_map[user_id] = hash_map.get(user_id , 0)+1
    print(f"The count is updated to : {hash_map[user_id]}")
    

# def generateRequest(key) :
    
#     return response


@shared_task(bind = True)
def getApiData(self):
    random_number = random.randint(0,1)
    news_request_data = [NEWS_API_EVERYTHING_GET_REQUEST , NEWS_API_TOP_HEADLINES_GET_REQUEST][random_number]
    # news_request_data = [NEWS_API_EVERYTHING_GET_REQUEST , NEWS_API_TOP_HEADLINES_GET_REQUEST][key]
    response = requests.get(
        url = news_request_data["url"] , 
        params = news_request_data["parameters"] , 
    )
    print(f"This is url : {news_request_data['url']}")
    print(f"This is parameters : {news_request_data['parameters']}")
    data            = dict(response.json())
    article         = data["articles"][0]
    source_id       = article["source"]["id"]
    source_name     = article["source"]["name"]
    author          = article["author"]
    title           = article["title"]
    description     = article["description"] if article["description"] else ""
    url             = article["url"]
    published_at    = article["publishedAt"]
    content         = article["content"] if article["content"] else ""
    published_at = datetime.fromisoformat(published_at[:-1])
    
    news = News.objects.create(
    source_id                           = source_id , 
    source_name                         = source_name , 
    author                              = author , 
    title                               = title , 
    description                         = description[:150] , 
    url                                 = url , 
    published_at                        = published_at , 
    content                             = content[:500] , 
    )
    print(news)
