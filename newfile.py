#this is a basic reddit comment crawler, based on input link

import time
import requests
import requests.auth
import praw
import re
from prawcore.exceptions import Forbidden
from praw.models import MoreComments
import sys

reddit = praw.Reddit(client_id='YourAppID',
                     client_secret='YourAppSecret',
                     user_agent = 'Complex user agent/client for development',
                     username ='YourUserHere',
                     password ='YourPassHere')

print(reddit.read_only)
print("Please enter the link of the post to crawl:")
url = input()
print("What would you like to save the output file as? Please end it in .txt")
file_path = input()

def get_post_id(url):
    pattern = r'(?<=comments\/)\w+'
    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        return None

post_id = get_post_id(url)
print(post_id)
submission = reddit.submission(post_id)

def commentPull():

    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        comments = top_level_comment.body
        file = open(file_path, "a")
        file.write(comments)
        file.close()
        print("String saved to file!")
        

commentPull()
