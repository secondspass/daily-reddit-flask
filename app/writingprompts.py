#!/usr/bin/env python3

# Script to download the highest response from the
# highest rated writing prompt on reddit's r/writingprompts
# subreddit in the past 24 hours

import praw


def getItems():
    most_upvotes = 0
    top_comment = None
    user_agent = "Daily top writingprompts by noirdragon"
    r = praw.Reddit(user_agent)
    subreddit = r.get_subreddit("writingprompts")
    writingprompt = subreddit.get_top_from_day(limit=1)
    for submission in writingprompt:
        for comment in submission.comments:
            try:
                if comment.is_root:
                    if comment.ups > most_upvotes:
                        most_upvotes = comment.ups
                        top_comment = comment
            except AttributeError:
                continue
        return (submission, top_comment)


def get_writingprompt():
    '''Returns the title, content and author of /r/writingprompts top
    submission today
    '''

    submission, top_comment = getItems()
    title = submission.title
    author = top_comment.author
    permalink = submission.permalink

    if title.find('[PI]') > -1:
        # If the submission is a [PI] submission
        content = submission.selftext

    elif title.find('[IP]') > -1:
        # If the submission is an Image Prompt
        link_start = submission.selftext.find('(') + 1
        link_end = submission.selftext.find(')')
        link = submission.selftext[link_start:link_end]
        content = '<img src=' + link + '>Image </img>' + '\n\n' + top_comment.body

    else:
        content = top_comment.body

    return (title, content, author, permalink)
