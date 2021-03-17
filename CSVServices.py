"""
For saving and reading our stats and a Elon quote AND for importing keywords
"""

import pandas as pd


class CSVServices:

    def __init__(self):
        self.data = pd.read_csv("database.csv")
        self.quotes = pd.read_csv("quotes.csv")

        try:
            self.laster_day = pd.read_csv("yesterday.csv")
        except:
            print("YESTERDAY DOESNT EXIST AHHHHHHH")

    def get_data_today(self, field):
        return self.data.loc[self.data["Key_Words"] == field, "Count"]

    def get_data_yesterday(self, field):
        try:
            return self.laster_day.loc[self.data["Key_Words"] == field, "Count"]
        except:
            return 0

    def write_data(self, field):
        self.data.loc[self.data["Key_Words"] == field, "Count"] += 1
        self.data.to_csv("database.csv", index=False)

    def night_save(self):
        self.data.to_csv("yesterday.csv", index=False)

    def quote_to_array(self):

        quotes = []

        for i in self.quotes:
            if type(i) is not str:
                continue
            else:
                quotes.append(i)

        return quotes
