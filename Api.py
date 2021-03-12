from aiohttp import ClientSession
import random
import praw


def daily_meme():
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
    top = subreddit.top(limit=10)
    for submission in top:
        all_submissions.append(submission)

    # Randomly selects from the top 10 submissions we pulled
    random_submission = random.choice(all_submissions)
    # Url for easy use in HTML Email
    url = random_submission.url
    print(url)


def daily_dadjoke():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    # Authenticate with our API key to pull random joke
    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': DAD_JOKE_API
    }

    # Requesting joke as JSON to parse the jokes setup/punchline
    async with ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            r = await response.json()
            r = r["body"][0]
            print(r["setup"])
            print(r["punchline"])
