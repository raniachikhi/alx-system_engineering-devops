#!/usr/bin/python3
"""Task 0"""

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid API request issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check if the response is a redirect (invalid subreddit)
        if response.status_code == 302:
            return 0

        # Parse the JSON response and extract the number of subscribers
        subreddit_info = response.json().get('data', {})
        subscribers_count = subreddit_info.get('subscribers', 0)

        return subscribers_count

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return 0
