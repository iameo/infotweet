import tweepy

import os
from dotenv import load_dotenv
from .models import TwitterUser

load_dotenv()


class TwitterAPI:
    def __init__(self):
        self.api_key = os.getenv('CONSUMER_API_KEY')
        self.api_secret = os.getenv('CONSUMER_API_SECRET')
        self.client_id = os.getenv('TWITTER_CLIENT_ID')
        self.client_secret = os.getenv('TWITTER_CLIENT_SECRET')
        self.oauth_callback_url = os.getenv('TWITTER_OAUTH_CALLBACK_URL')

    def twitter_login(self):
        oauth1_user_handler = tweepy.OAuthHandler(self.api_key, self.api_secret, callback=self.oauth_callback_url)
        url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)
        request_token = oauth1_user_handler.request_token["oauth_token"]
        request_secret = oauth1_user_handler.request_token["oauth_token_secret"]
        return url, request_token, request_secret

    def twitter_callback(self,oauth_verifier, oauth_token, oauth_token_secret):
        oauth1_user_handler = tweepy.OAuthHandler(self.api_key, self.api_secret, callback=self.oauth_callback_url)
        oauth1_user_handler.request_token = {
            'oauth_token': oauth_token,
            'oauth_token_secret': oauth_token_secret
        }
        access_token, access_token_secret = oauth1_user_handler.get_access_token(oauth_verifier)
        return access_token, access_token_secret

    def get_me(self, access_token, access_token_secret):
        try:
            client = tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret, access_token=access_token,
                                   access_token_secret=access_token_secret, wait_on_rate_limit=True)
            info = client.get_me(user_auth=True, expansions='pinned_tweet_id', user_fields='profile_image_url')
            
        except Exception as e:
            return None
        return info
    
    # def tweepy_client(self):
    #     user = TwitterUser.objects.filter(user=request.user)
    #     try:
    #         client = tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret, access_token=user.twitter_oauth_token.oauth_token,
    #                                access_token_secret=user.twitter_oauth_token.oauth_token_secret, wait_on_rate_limit=True)
    #     except Exception as e:
    #         return None
    #     return client