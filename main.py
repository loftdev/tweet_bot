from tweet import Tweet
from like import like
from search_and_like import search_like
from error_handler import InputErrorHandling


user_input = input('Enter "t" if you want to tweet from csv file, '
                   '"l" if you like to "Like" from your timeline, '
                   '"s" if you want to search and like the top result: ').lower()

user_request = InputErrorHandling(user_input).wrong_input()


if user_request == "t":
    Tweet().tweet_sort()

elif user_request == "l":
    like()

elif user_request == "s":
    search_like()

else:
    print("You entered wrong data")
