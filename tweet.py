from TwitterAPI_class import api
import csv
import tweepy
from error_handler import DataChecker

csvFilePath = "csv_file/product_info.csv"
file = DataChecker(csvFilePath).check_csv()


def tweet():
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        print("Tweeting")
        for row in csv_reader:
            # print(row[1])
            try:
                api.update_status(row[1])
                print(row[1])
            except tweepy.error.TweepError as e:
                if e.api_code == 187:
                    continue
                else:
                    print("API error")
