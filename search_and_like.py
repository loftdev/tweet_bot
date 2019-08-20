from TwitterAPI_class import api


def search_like():
    keyword = input("Enter topics you want to search: ")
    search_ = api.search(q=keyword, count=15)
    searched = search_[0]
    api.create_favorite(searched.id)
    print(f"liked {searched.id} of {searched.author.name}")
