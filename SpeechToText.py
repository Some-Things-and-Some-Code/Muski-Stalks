"""
Class by Baron
"""

import speech_recognition as sr
import pandas as pd
import pyttsx3
import csv
import os


class SpeechToText:

    def __init__(self):
        self.EMERGENCY_SHUTDOWN = "marmalade"

        # make sure the file is there or create it if it isn't
        try:
            if os.path.isfile('database.csv'):
                csv_file = open('database.csv', 'a', encoding='utf-8-sig', newline='')
                csv_file.close()
            # If the file does not exist, creates it
            else:
                csv_file = open('database.csv', 'w', encoding='utf-8-sig', newline='')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Key_Words', 'Count'])
                csv_file.close()
        except Exception as e:
            print(e)
            exit()

    # Function for the program to speak text sent to the function
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Function to listen to audio
    def get_audio(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # r.energy_threshold = 2300
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
            except Exception as e:
                print("Exception:", str(e))

        return said.lower()

    def word_tracker(self):
        print("Listening to surroundings...")

        # Starts our listener and returns the text detected
        text = self.get_audio()
        # Splits all words heard into an array
        text = text.split(" ")
        print(text)
        # Checks the array for keywords and updates the database with how many times they have been mentioned
        for word in text:
            if word.find(self.EMERGENCY_SHUTDOWN) != -1:  # stop loop
                print("Exiting Program...")
                exit()

            elif word == "elan" or word == "ilan" or word == "elon":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Elon", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "musk":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Musk", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "muskie" or word == "musky":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Musky", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "boy" or word == "boi":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Boi", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "tesla":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Tesla", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "spacex":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "SpaceX", "Count"] += 1
                df.to_csv("database.csv", index=False)

            elif word == "mars":
                df = pd.read_csv('database.csv')
                df.loc[df["Key_Words"] == "Mars", "Count"] += 1
                df.to_csv("database.csv", index=False)

            else:
                continue
