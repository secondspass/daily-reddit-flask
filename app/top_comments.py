#!/usr/bin/env python3

# Script to download the highest rated comment from the
# highest rated post of the past 24 hours from the given subreddit

import praw


def getItems(subreddit):
    most_upvotes = 0
    top_comment = None
    user_agent = "Daily top comment by noirdragon"
    r = praw.Reddit(user_agent)
    subreddit_obj = r.get_subreddit(subreddit)
    posts = subreddit_obj.get_top_from_day(limit=1)
    for post in posts:
        for comment in post.comments:
            try:
                if comment.is_root:
                    if comment.ups > most_upvotes:
                        most_upvotes = comment.ups
                        top_comment = comment
            except AttributeError:
                continue
        return (post, top_comment)


def get_top_comment(subreddit):
    '''Returns the title, content, author of the top comment and
    the link of the top post of the last 24 hours from the given subreddit.
    '''

    post, top_comment = getItems(subreddit)
    title = post.title
    permalink = post.permalink
    content = top_comment.body
    author = top_comment.author

    return (title, content, author, permalink)
