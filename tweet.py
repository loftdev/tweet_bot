from TwitterAPI_class import api
import csv
import tweepy

csvFilePath = "for_tweet/product_info.csv"


def tweet():
    with open(csvFilePath, mode='r') as csv_file:
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
