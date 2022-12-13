import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "DzFjmdkX3FPe2DuU1Chq7dVL1"
# api secret key
api_secret_key = "5tkOOYNbrao87OBZ8XshNZ4faLFU6YaRFR6sjysPOtW4zVfww2"
# access token
access_token = "1601512983372263424-ayoF9uGLE68Y3IVr7YjIkM91cuD9wa"
# access token secret
access_token_secret = "qGxbRq03cfUdIWT0Ee90Rj5pdPPN9xI2UrdXB6aIq5m6A"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)


def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 20
    try:
        # Pulling individual tweets from query
        for tweet in api.search_tweets(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)