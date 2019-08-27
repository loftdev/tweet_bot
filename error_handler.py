import re
# import tweepy
import os.path


class DataChecker:
    def __init__(self, check_data):
        self.check_data = check_data
        self.data_type = "[tls]"

    def check_data_long(self):
        count = 0
        while count < 3:
            if len(self.check_data) > 20:
                count += 1
                data = input("You exceed the number of character to be entered! limit 20 only!")
                return data
            else:
                return self.check_data

    def check_data_short(self):
        data = self.check_data
        count = 0
        for i in range(4):
            x = re.findall(self.data_type, data)
            if len(data) > 1:
                count += 1
                data = input(f"You exceed the number of character to be entered! try remaining {4 - count}! ")
            else:

                if not x:
                    count += 1
                    data = input(f"Enter the right letter again! try remaining {4 - count}! ")

                elif x[0] == "t" or x[0] == "l" or x[0] == "s":
                    return data
                else:
                    count += 1
                    data = input(f"Enter the right letter again! try remaining {4 - count}! ")

    def check_csv(self):
        file = self.check_data
        if os.path.exists(file):
            print(os.path.exists(file))
            if os.path.isfile(file):
                return file
            else:
                print("There is no file")
        else:
            print("Directory does not exist")


"""
class APIChecker:
    def __init__(self, test_data):
        self.test_data = test_data

    def api_error(self):
        try:
            self.test_data
        except tweepy.error.TweepError:
            print("API error")
"""

"""
class ErrorConstraints:
    def __init__(self, data):
        self.data = data

    def data_check(self):
        if len(self.data) > 1:
            return print("Entered data must be one letter only! ")

        try:
            int(self.data)
            data_type = "int"
        except ValueError:
            data_type = "str"

        if data_type == "int":
            return print("Entered data is not a letter! ")

    def search_data_check(self):
        if len(self.data) > 20:
            return print("Entered data is too long, input limit is 20 character only! ")


x = input("enter a letter: ")
ErrorConstraints(x).search_data_check()
"""
