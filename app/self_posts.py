#!/usr/bin/env python3

# Script to download the highest rated self post of the last 24 hours from
# the given subreddit

import praw


def getItems(subreddit):
    user_agent = "Daily top self post by noirdragon"
    r = praw.Reddit(user_agent)
    subreddit_obj = r.get_subreddit(subreddit)
    posts = subreddit_obj.get_top_from_day(limit=1)
    for post in posts:
        return post


def get_self_post(subreddit):
    self_post = getItems(subreddit)
    title = self_post.title
    content = self_post.selftext
    author = self_post.author
    permalink = self_post.permalink
    return (title, content, author, permalink)
