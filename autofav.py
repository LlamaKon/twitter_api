# -*- coding: utf-8 -*-

import datetime

import tweepy

from config import CONFIG


CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create an instance
api = tweepy.API(auth)

# Find Tweets
def autofav():
    q_list = ["python","Java","#駆け出しエンジニアと繋がりたい","#プログラミング初心者"]
    count  = 50
    for q in q_list:
        search_results = api.search(q=q, count=count)
        for result in search_results:
            tweet_id = result.id
            try:
                api.create_favorite(tweet_id)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    autofav()
