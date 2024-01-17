#!/usr/bin/python3
"""Task 2 """
import requests

def recurse(subreddit, hot_list=[], after=None):
    if after is None and not is_valid_subreddit(subreddit):
        return None

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    params = {'after': after} if after else {}

    try:
        response = requests.get(api_url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 302:
            return None

        posts = response.json().get('data', {}).get('children', [])

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        next_page_after = response.json().get('data', {}).get('after')
        if next_page_after:
            recurse(subreddit, hot_list, next_page_after)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

    return hot_list

def is_valid_subreddit(subreddit):
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        return response.status_code != 302

    except requests.exceptions.RequestException as e:
        print(f"Error checking subreddit validity: {e}")
        return False
