import tweepy
from twitter_credentials import access_token, access_token_secret, consumer_key, consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)