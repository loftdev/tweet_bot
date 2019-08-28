import re
import pathlib


class InputErrorHandling:
    def __init__(self, input_data):
        self.input_data = input_data
        self.data_type = "[tls]"

    def exceed_limit(self):
        count = 0
        for i in range(4):
            if len(self.input_data) > 20:
                count += 1
                data = input(f"You exceed the number of character to be entered! limit 20 only! try remaining {4 - count}")
                return data
            else:
                return self.input_data

    def wrong_input(self):
        data = self.input_data
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
        file = self.input_data
        path = pathlib.Path(file)
        if path.exists():
            return file
        else:
            print("File not found")
