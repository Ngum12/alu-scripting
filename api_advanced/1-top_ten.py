#!/usr/bin/python3
"""Writing a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                json_data.get('data')
                .get('children')[i]
                .get('data')
                .get('title')
            )
    else:
        print(None)
