#!/usr/bin/env python

import praw
import re
import yaml

reddit = praw.Reddit(client_id='xx',
                     client_secret="xx",
                     password='xx',
                     user_agent='xx',
                     username='xx')

new_data = {}

num_posts = 100

subreddit = reddit.subreddit('dailyprogrammer')

for submission in subreddit.hot(limit=num_posts):
    
    new_data[submission.id] = {
        'title' : submission.title,
        'url' : submission.url,
        'solutions' : [],
    }

    submission.comments.replace_more(limit=0)
    all_comments = submission.comments.list()

    for comment in all_comments:
        if re.search('(perl6|perl 6)', comment.body, re.I):

            new_data[submission.id]['solutions'].append({
                'solution_url' : 'https://www.reddit.com' + comment.permalink(),
                'solution_body' : comment.body,
            })

with open('perl6_daily_programmer.yaml', 'w+') as file:
    old_data = yaml.safe_load(file)
    if old_data:
        temp = {}
        temp.update(old_data)
        temp.update(new_data)
        yaml.dump(temp, file, default_flow_style=False)
    else:
        yaml.dump(new_data, file, default_flow_style=False)
