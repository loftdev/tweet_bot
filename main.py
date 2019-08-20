from error_handling import error_handling
from tweet import tweet
from like import like
from search_and_like import search_like

user_request = input('Enter "t" if you want to tweet from csv file, '
                     '"l" if you like to "Like" from your timeline, '
                     '"sl" if you wan to search and like the top result: ').lower()

if user_request == "t":
    error_handling(tweet())
elif user_request == "l":
    error_handling(like())
elif user_request == "sl":
    error_handling(search_like())
else:
    print("You entered wrong data")
