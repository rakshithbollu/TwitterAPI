import tweepy
from tweepy import OAuthHandler
import pandas as pd


class TwitterClient(object): 
    def __init__(self):
        # Access Credentials 
        consumer_key = 'DzFjmdkX3FPe2DuU1Chq7dVL1'
        consumer_secret = '5tkOOYNbrao87OBZ8XshNZ4faLFU6YaRFR6sjysPOtW4zVfww2'
        access_token = '1601512983372263424-ayoF9uGLE68Y3IVr7YjIkM91cuD9wa'
        access_token_secret = 'qGxbRq03cfUdIWT0Ee90Rj5pdPPN9xI2UrdXB6aIq5m6A'
        # OAuthHandler object 
        auth = OAuthHandler(consumer_key, consumer_secret) 
        # set access token and secret 
        auth.set_access_token(access_token, access_token_secret) 
        # create tweepy API object to fetch tweets 
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

        if self.api.verify_credentials() == False:
            print("user creds are invalid")
        else:
            print("valid user")


        
            
    
    
    # We are keeping cleaned tweets in a new column called 'tidy_tweets'
   

    # Function to fetch tweets
    def get_tweets(self, query, maxTweets = 100): 
        # empty list to store parsed tweets 
        tweets = [] 
        sinceId = None
        max_id = -1
        tweetCount = 0
        tweetsPerQry = 100
        
        while tweetCount < maxTweets:
            
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry)
                else:
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                else:
                    new_tweets = self.api.search_tweets(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
                    
            for tweet in new_tweets:
                parsed_tweet = {} 
                parsed_tweet['tweets'] = tweet.text 

                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
                        
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id

            
        
        return pd.DataFrame(tweets)