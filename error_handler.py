import re


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
        x = re.findall(self.data_type, data)
        count = 0
        while count < 4:
            if len(data) > 1:
                count += 1
                data = input("You exceed the number of character to be entered! Enter again!")
                return data
            else:
                if x == "t" or x == "l" or x == "s":
                    return self.user_input
                else:
                    count += 1
                    data = input("Enter the right letter again!")
                    return data
