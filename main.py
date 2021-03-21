"""
Controller for the thing
"""

from EmailServices import *
from SpeechToText import *
from datetime import datetime


def main():

    # Initialize child functions
    es = EmailServices()
    stt = SpeechToText()

    while True:

        # Keep track of our words
        stt.word_tracker()

        # get the current hour
        now = datetime.now()

        hour = now.strftime("%H")

        if hour == "08":
            es.send_email()
            es.csv.night_save()
            es.csv.zero_fill()


if __name__ == '__main__':
    main()
