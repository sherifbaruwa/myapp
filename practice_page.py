import tweepy
import time

auth = tweepy.OAuthHandler("RreaSVxjRjPv9rAp3K6IEhLr2", "uZb25nD8xSN5Dp6fs9YiI6k0TzvFbhBeAdsXiUxbQDEOQb5jof")
auth.set_access_token("207395623-LFmolsMCyutV7hN05E1fDfJwYjBV91JMlcyscu6J", "6pIfRbOmact0OqN2RfR1677ZJ41nOelFvnC3tO5qVy67r")

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



# hello world
