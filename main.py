from tweet import tweet_sort
from like import like
from search_and_like import search_like
from input_handler import one_letter_input
import tweepy


user_input = input('Enter "t" if you want to tweet from csv file, '
                   '"l" if you like to "Like" from your timeline, '
                   '"s" if you want to search and like the top result: ').lower()
input_data = one_letter_input(user_input)


if input_data == "t":
    try:
        tweet_sort()
    except tweepy.error.TweepError:
        print("API error")

elif input_data == "l":
    try:
        like()
    except tweepy.error.TweepError:
        print("API error")

elif input_data == "s":
    try:
        search_like()
    except tweepy.error.TweepError:
        print("API error")

else:
    print("You entered wrong data")
