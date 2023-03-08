
import os
import twitter
from rest_framework import serializers


from dotenv import load_dotenv
load_dotenv()


class TwitterAuthTokenVerification:
    @staticmethod
    def validate_access_tokens(access_token_key, access_token_secret):
        consumer_api_key = os.getenv('CONSUMER_API_KEY')
        consumer_api_Secret= os.getenv('CONSUMER_API_SECRET')

        try:
            api = twitter.Api(
                consumer_key=consumer_api_key,
                consumer_secret=consumer_api_Secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret
            )
            user_profile = api.VerifyCredentials(include_email=True)
        except Exception as e:
            raise serializers.ValidationError({
                "tokens": ["The tokens are invalid"],
                "error": str(e)
            })
        else:
            return user_profile
