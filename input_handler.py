import re
import pathlib


def one_letter_input(x):
    data = x
    count = 0
    expected_data = "[tls]"
    for i in range(3):
        x = re.findall(expected_data, data)
        if len(data) > 1:
            count += 1
            data = input(f"You exceed the number of character to be entered! "
                         f"try remaining {4 - count}! ")

        elif not x:
            count += 1
            data = input(f"Enter the right letter again! try "
                         f"remaining {4 - count}! ")

        elif x[0] == "t" or x[0] == "l" or x[0] == "s":
            return data

    return print("You entered wrong data")


def keyword_input(x):
    data = x
    count = 0
    for i in range(4):
        if len(data) > 20:
            count += 1
            data = input(f"You entered {len(data)}! limit 20 only! try "
                         f"remaining {4 - count}! ")
        else:
            return data


def csv_data(x):
    path = pathlib.Path(x)
    if path.exists():
        return x
    else:
        print("File not found")
