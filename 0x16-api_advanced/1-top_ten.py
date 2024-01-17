#!/usr/bin/python3
"""Task 1"""

import requests

def top_ten(subreddit):
    """Top ten """
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 302:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])

        for i, post in enumerate(posts[:10]):
            title = post['data']['title']
            print(f"{i + 1}. {title}")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        print(None)
