
import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
access_token = "813768169223585794-kymypAp5EqMRB311O28o3W2LM1TwXt9"
access_token_secret = "TCBKBFTvhI2FUq6IxoF7hI3NoyHq3PwbH9ukrdLTCNQB6"
consumer_key = "ixExcutvFASjfzv8LxrH5o90r"
consumer_secret = "T7jVg9O5ZdvvAaJgW1GR9tlAjl8SwJTOE4dK9IR6IbLPCHyFDY"

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        tweeter = json.loads(data)
        for url in tweeter["entities"]["urls"]:
            print "%s" % url["expanded_url"] + "\r\n"

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['www.', 'vimeo', 'reddit', 'bleacher report'])