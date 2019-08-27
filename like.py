from TwitterAPI_class import api
import tweepy


def like():
    try:
        tweets = api.home_timeline(count=3)
        tweet = tweets[0]
        print("Liking")
        print(f"Tweet {tweet.id} of {tweet.author.name}")
        api.create_favorite(tweet.id)
    except tweepy.error.TweepError:
        print("API error")

