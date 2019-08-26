import re
import tweepy


class DataChecker:
    def __init__(self, user_input, data_type):
        self.user_input = user_input
        self.data_type = data_type

    def check_data_long(self):
        count = 0
        while count < 3:
            if len(self.user_input) > 20:
                count += 1
                data = input("You exceed the number of character to be entered! between 1-20 only")
                return data
            else:
                return self.user_input

    def check_data_short(self):
        data = self.user_input
        count = 0
        while count < 3:
            x = re.findall(self.data_type, data)
            print(x)
            print(len(data))
            if len(data) > 1:
                data = input(f"You exceed the number of character to be entered! try remaining {3 - count}! ")
                count += 1
            else:

                if not x:
                    print(len(x))
                    data = input(f"Enter the right letter again! try remaining {3 - count}! ")
                    count += 1
                elif x[0] == "t" or x[0] == "l" or x[0] == "s":
                    return data
                else:
                    data = input(f"Enter the right letter again! try remaining {3 - count}! ")
                    count += 1


class APIChecker:
    def __init__(self, test):
        self.test = test

    def api_error(self):
        try:
            self.test
        except tweepy.error.TweepError:
            print("API error")
