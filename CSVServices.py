"""
For saving and reading our stats and a Elon quote AND for importing keywords
"""

import pandas as pd


class CSVServices:

    def __init__(self):
        self.data = pd.read_csv("database.csv")

    def get_data(self, field):
        return self.data.loc[self.data["Key_Words"] == field, "Count"]

    def write_data(self, field):
        pass
