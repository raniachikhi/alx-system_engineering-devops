#!/usr/bin/python3
"""Task 0"""

import requests

def number_of_subscribers(subreddit):
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 302:
            return 0

        subreddit_info = response.json().get('data', {})
        subscribers_count = subreddit_info.get('subscribers', 0)

        return subscribers_count

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return 0
