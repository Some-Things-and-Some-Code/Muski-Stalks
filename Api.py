from secrets import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT, DAD_JOKE_API
import requests
import random
import praw


class Api:
    def daily_meme(self):
        # Pulling authentication variables from ENV
        reddit = praw.Reddit(client_id=CLIENT_ID,
                             client_secret=CLIENT_SECRET,
                             username=USERNAME,
                             password=PASSWORD,
                             user_agent=USER_AGENT)

        # Selecting the r/memes subreddit
        subreddit = reddit.subreddit("memes")
        # Creating an array to store the top 10 submissions
        all_submissions = []
        top = subreddit.top(limit=2)
        for submission in top:
            all_submissions.append(submission)

        # Randomly selects from the top 10 submissions we pulled
        random_submission = random.choice(all_submissions)
        # Url for easy use in HTML Email
        url = random_submission.url
        print(url)

        return url

    def daily_dadjoke(self):
        url = "https://dad-jokes.p.rapidapi.com/random/joke"

        # Authenticate with our API key to pull random joke

        # Requesting joke as JSON to parse the jokes setup/punchline
        response = requests.get(url,
                                headers={
                                    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
                                    'x-rapidapi-key': DAD_JOKE_API
                                })

        r = response.json()
        r = r["body"][0]

        setup = r["setup"]
        punchline = r["punchline"]

        print(f"{setup}\n{punchline}")
        return setup, punchline

# api = Api()
# api.daily_dadjoke()
# api.daily_meme()
