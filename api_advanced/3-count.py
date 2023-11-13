#!/usr/bin/python3
"""count it"""

import json
import requests


def count_words(subreddit, word_list, after='', hot_list=[]):
    """Function that queries the Reddit API."""
    if after == '':
        hot_list = [0] * len(word_list)
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'My API advanced 1.0'})
    if request.status_code == 200:
        data = request.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        hot_list[i] += 1

        after = data['data']['after']
        if after is None:
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        hot_list[i] += hot_list[j]
                        hot_list[j] = 0

            sorted_words = sorted(zip(word_list, hot_list), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_words:
                if count > 0:
                    print(f"{word.lower()}: {count}")
        else:
            count_words(subreddit, word_list, after, hot_list)


# Example usage
subreddit_name = "unpopular"
keywords_list = ['you', 'unpopular', 'vote', 'down', 'downvote', 'her', 'politics']
count_words(subreddit_name, keywords_list)

