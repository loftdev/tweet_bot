from TwitterAPI_class import api


def like():
    tweets = api.home_timeline(count=3)
    tweet = tweets[0]
    print("Liking")
    print(f"Tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)

