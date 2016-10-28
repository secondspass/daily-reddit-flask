from flask import render_template
from flask import Markup
import re
from . import writingprompts
from . import jokes
from app import app

subreddit_list = [
    {'name': 'writingprompts', 'title': 'Writing Prompts', 'function': writingprompts.get_writingprompt},
    {'name': 'jokes', 'title': 'Jokes', 'function': jokes.get_joke}
]


@app.route('/')
def index():
    return render_template('index.html',
                           subredditlist=subreddit_list
                           )


@app.route('/<post>/')
def todays_post(post):
    for subreddit in subreddit_list:
        if post == subreddit['name']:
            post_title, content, author, permalink = subreddit['function']()
            content = insert_linebreaks(content)
            return render_template('post.html',
                                   subredditname=subreddit['title'],
                                   content=Markup(content),
                                   post_title=post_title,
                                   author=author,
                                   permalink=permalink
                                   )

    return render_template('404.html')


def insert_linebreaks(content):
    '''Converts the line breaks in the content of the post to <br> tags
    '''

    content = re.sub(r'\n', '<br>', content)
    return content
