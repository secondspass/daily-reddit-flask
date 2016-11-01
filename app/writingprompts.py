#!/usr/bin/env python3

# Script to download the highest rated response from the
# highest rated writing prompt on reddit's r/writingprompts
# subreddit in the past 24 hours

from . import top_comments


def get_writingprompt(subreddit):
    '''Returns the title, content and author of the top response of the top
    post and the link to the top post in /r/writingprompts of today.
    '''

    post, top_comment = top_comments.getItems(subreddit)
    title = post.title
    author = top_comment.author
    permalink = post.permalink

    if title.find('[PI]') > -1:
        # If the post is a [PI] submission
        content = post.selftext
        author = post.author

    elif title.find('[IP]') > -1:
        # If the post is an Image Prompt
        link_start = post.selftext.find('(') + 1
        link_end = post.selftext.find(')')
        link = post.selftext[link_start:link_end]
        content = '<img src=' + link + '>Image </img>' + '\n\n' + top_comment.body

    else:
        content = top_comment.body

    return (title, content, author, permalink)
