#!/usr/bin/env python3

# Script to download the highest rated joke on reddit's r/jokes subreddit in the 
# past 24 hours

import praw


def getItems():
    user_agent = "Daily top jokes by noirdragon"
    r = praw.Reddit(user_agent)
    subreddit = r.get_subreddit("jokes")
    joke = subreddit.get_top_from_day(limit=1)
    for submission in joke:
        return submission


def get_joke():
    joke_submission = getItems()
    title = joke_submission.title
    content = joke_submission.selftext
    author = joke_submission.author
    permalink = joke_submission.permalink
    return (title, content, author, permalink)
