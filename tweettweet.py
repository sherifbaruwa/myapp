import tweepy
import time

auth = tweepy.OAuthHandler("RreaSVxjRjPv9rAp3K6IEhLr2", "uZb25nD8xSN5Dp6fs9YiI6k0TzvFbhBeAdsXiUxbQDEOQb5jof")
auth.set_access_token("207395623-LFmolsMCyutV7hN05E1fDfJwYjBV91JMlcyscu6J", "6pIfRbOmact0OqN2RfR1677ZJ41nOelFvnC3tO5qVy67r")

api = tweepy.API(auth)
user = api.me()

# limit handler
# def limit_handler(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)


# like tweets with specific key words
# search_string = 'python'
# numberOfTweets = 2

# for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print('i like that tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break


# # super generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.screen_name == "kiing_ot":
#         follower.follow()

#     # print(follower.screen_name)
