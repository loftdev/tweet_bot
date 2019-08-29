from TwitterAPI_class import api
from input_handler import keyword_input
import tweepy


def search_like():
    user_input_keyword = input("Enter topics you want to search: ")
    keyword = keyword_input(user_input_keyword)
    search_ = api.search(q=keyword, count=15)
    searched = search_[0]
    try:
        api.create_favorite(searched.id)
        print(f"liked {searched.id} of {searched.author.name}")
    except tweepy.error.TweepError:
        print("API error")
