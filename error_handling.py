import tweepy


def error_handling(x):

    try:
        x
    except tweepy.error.TweepError as e:
        print(e.reason)

