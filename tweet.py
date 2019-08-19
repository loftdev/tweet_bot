from TwitterAPI_class import api
import csv

csvFilePath = "for_tweet/product_info.csv"


def tweet():
    with open(csvFilePath, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # print(row[1])
            try:
                api.update_status(row[1])
            except:
                continue
