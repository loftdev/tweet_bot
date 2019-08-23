from tweet import tweet
from like import like
from search_and_like import search_like
import tweepy
from error_handler import DataChecker

user_input = input('Enter "t" if you want to tweet from csv file, '
                   '"l" if you like to "Like" from your timeline, '
                   '"s" if you wan to search and like the top result: ').lower()

user_request = DataChecker(user_input, "[tls]").check_data_short()


if user_request == "t":
    try:
        tweet()
    except tweepy.error.TweepError as e:
        print(e.reason)
elif user_request == "l":
    try:
        like()
    except tweepy.error.TweepError as e:
        print(e.reason)
elif user_request == "s":
    try:
        search_like()
    except tweepy.error.TweepError as e:
        print(e.reason)
else:
    print("You entered wrong data")
