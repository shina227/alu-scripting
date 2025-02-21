#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot posts.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
                
    Args:
        subreddit (str): The name of the subreddit.
                                
    Returns:
        None: Prints the top 10 hot post titles or None if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom-user-agent"}
                                                            
    response = requests.get(url, headers=headers, allow_redirects=False)
                                                                    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
                                                                                                                                    
