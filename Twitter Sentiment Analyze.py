#It will be able to search twitter for a list of tweets about any topic we want, 
#then analyze each tweet to see how positive or negative it's emotion is. 
#Here we do this with the help of an API textblob. 
#-@harish_2194

import tweepy
from textblob import TextBlob

# Authentication via code
consumer_key = "CONSUMER_KEY_HERE"
consumer_secret = "CONSUMER_SECRET_HERE"

access_token = "ACCESS_TOKEN_HERE"
access_token_secret = "ACCESS_TOKEN_SECRET_HERE"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#main code
api = tweepy.API(auth)

user_tweets = api.search('pranushka')

for tweet in user_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.words)
	print(analysis.sentiment)
	


