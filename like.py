from TwitterAPI_class import api


def like():
    tweets = api.home_timeline(count=)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)
