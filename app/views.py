from flask import render_template
from flask import Markup
import re
from . import writingprompts
from . import self_posts
from app import app

subreddit_list = [
    {'name': 'writingprompts', 'title': 'Writing Prompts', 'function': writingprompts.get_writingprompt},
    {'name': 'nosleep', 'title': 'No Sleep', 'function': self_posts.get_self_post},
    {'name': 'jokes', 'title': 'Jokes', 'function': self_posts.get_self_post},
    {'name': 'meanjokes', 'title': 'Mean Jokes', 'function': self_posts.get_self_post},
    {'name': 'fantheories', 'title': 'Fan Theories', 'function': self_posts.get_self_post},
    {'name': 'letsnotmeet', 'title': 'Lets Not Meet', 'function': self_posts.get_self_post},
    {'name': 'talesfromtechsupport', 'title': 'Tales From Tech Support', 'function': self_posts.get_self_post},
    {'name': 'talesfromretail', 'title': 'Tales From Retail', 'function': self_posts.get_self_post},
    {'name': 'talesfromsecurity', 'title': 'Tales From Security', 'function': self_posts.get_self_post},
    {'name': 'talesfromyourserver', 'title': 'Tales From Your Server', 'function': self_posts.get_self_post},
    {'name': 'talesfromthepharmacy', 'title': 'Tales From the Pharmacy', 'function': self_posts.get_self_post}
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
            post_title, content, author, permalink = subreddit['function'](post)
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
