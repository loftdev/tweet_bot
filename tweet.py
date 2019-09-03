from TwitterAPI_class import api
import csv
import tweepy
from input_handler import csv_data


csv_path = "csv_file/product_info.csv"


def tweet_all():
    file = csv_data(csv_path)
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        print("Tweeting")
        for row in csv_reader:
            try:
                api.update_status(row[1])
                print(row[1])
            except tweepy.error.TweepError as e:
                if e.api_code == 187:
                    continue
                else:
                    print("API error")


def tweet_sort():
    file = csv_data(csv_path)
    try:
        input_file = csv.DictReader(open(file))
    except TypeError:
        return print("No csv file")

    expensive_price = None
    expensive_product = None
    cheapest_price = None
    cheapest_product = None

    for row in input_file:
        age = int(row["Price"])
        if expensive_price is None or expensive_price < age:
            expensive_price = age
            expensive_product = row["Title"]

        if cheapest_price is None or cheapest_price > age:
            cheapest_price = age
            cheapest_product = row["Title"]

    if expensive_price is not None:
        result = (f"From the search result of top 30's most expensive iPad pro keyboard. "
                  f"the most expensive among the list is  {expensive_product}, the price is ¥{expensive_price}. "
                  f"the cheapest is {cheapest_product} for the price of ¥{cheapest_price}")
        api.update_status(result)
    else:
        print("The file does not contain any people.")


