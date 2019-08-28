from TwitterAPI_class import api
from error_handler import InputErrorHandling


def search_like():
    keyword_input = input("Enter topics you want to search: ")
    keyword = InputErrorHandling(keyword_input)
    search_ = api.search(q=keyword, count=15)
    searched = search_[0]
    api.create_favorite(searched.id)
    print(f"liked {searched.id} of {searched.author.name}")
