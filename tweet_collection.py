from apscheduler.schedulers.blocking import BlockingScheduler

import tweepy, sys, json
import re
reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key = 'lMAzPJAAkVabDtqhjvn1pbR5J'
consumer_secret = '8ljP62OevLuNhxfZP2iRttsgn7mthO5p7PXnyJCQfccqfAm21f'
access_token_key = '1454765689-NLBtaIgy7IaJLcfpAi9f4QcEitsMRqen9DyD0hS'
access_token_secret = '8DdgGB4J1VCH5OdrlebcwKLlmwfZsbvvj7DnEflSLZRhA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
myApi = tweepy.API(auth)

def tweet_collection():
    geo = "15.3173,75.7139,200mi"
    tweets = myApi.search(q='karnatakElection2018 OR karnatakaElection OR karnatakElection OR Congress OR Cong OR rahul OR RGinKarnatak OR karnatakElection2018 OR ExitPollKarnataka OR ExitPoll OR karnatakElections2018 OR CongressMuktBharat OR pappu OR CongreaaGayi OR congresscheatsdemocracy OR CongressExposed OR congressfails OR congresschor  ', count=1000, lang='en')
    for tweet in tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text
        String=tweet.text
        with open("CNG.txt", 'a+') as files:
           files.write(String)
           files.write("\n")
scheduler = BlockingScheduler()
scheduler.add_job(tweet_collection, 'interval', seconds=30)
scheduler.start()