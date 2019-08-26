from tweet import tweet
from like import like
from search_and_like import search_like
import tweepy
from error_handler import DataChecker, APIChecker


user_input = input('Enter "t" if you want to tweet from csv file, '
                   '"l" if you like to "Like" from your timeline, '
                   '"s" if you wan to search and like the top result: ').lower()

user_request = DataChecker(user_input, "[tls]").check_data_short()


if user_request == "t":
    APIChecker(tweet())
elif user_request == "l":
    APIChecker(like())
elif user_request == "s":
    APIChecker(search_like())
else:
    print("You entered wrong data")
