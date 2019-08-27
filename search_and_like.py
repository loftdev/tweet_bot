from TwitterAPI_class import api
from error_handler import DataChecker
import tweepy


def search_like():
    try:
        keyword = input("Enter topics you want to search: ")
        DataChecker(keyword).check_data_long()
        search_ = api.search(q=keyword, count=15)
        searched = search_[0]
        api.create_favorite(searched.id)
        print(f"liked {searched.id} of {searched.author.name}")
    except tweepy.error.TweepError:
        print("API error")
