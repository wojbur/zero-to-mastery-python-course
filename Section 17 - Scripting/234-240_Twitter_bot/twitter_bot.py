from pydoc import cli
from urllib import response
import tweepy
import json

# config.py : where I keep my keys as constants
# import config


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    """Return a list of latest ZTM tweets"""
    ztm = client.get_user(username="WKBurman")
    response = client.get_users_tweets(ztm.data.id)
    return response.data


if __name__ == "__main__":
    # load API keys from KEYS.json file
    with open("KEYS.json") as f:
        data = dict(json.load(f))
        bearer_token = data["Bearer Token"]
        consumer_key = data["API Key"]
        consumer_secret = data["API Key Secret"]
        access_token = data["Access Token"]
        access_token_secret = data["Access Token Secret"]

    # set up API client
    client = tweepy.Client(
        bearer_token = bearer_token,
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret,
    )

    # print("=== About Me ===")
    # about_me(client)
    # print()
    # print("=== ZTM Tweets ===")
    # for tweet in get_ztm_tweets(client):
    #     print(tweet, end="\n\n")

    # response = client.create_tweet(text='This Tweet was Tweeted using Tweepy and Twitter API v2!')
    # print(f"https://twitter.com/user/status/{response.data['id']}")
    ztm = client.get_user(username="zerotomasteryio")
    ztm_followers = client.get_users_followers(ztm.data.id)
    