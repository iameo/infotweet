from .twi_helper import TwitterAuthTokenVerification
from rest_framework import serializers

# from .register import register_user

class TwitterAuthSerializer(serializers.Serializer):
    access_token_key = serializers.CharField()
    access_token_secret = serializers.CharField()
    
    # def to_representation(self, value):
    #     """
    #     Serialize the value's class name.
    #     """
    #     print("to_rep", value, type(value))
    #     return value

    def validate(self, attrs):
        # print("attrs: ", attrs.get('access_token_key'))
        access_token_key = attrs.get('access_token_key')
        access_token_secret= attrs.get('access_token_secret')

        user_info = TwitterAuthTokenVerification.validate_access_tokens(
            access_token_key, access_token_secret
        )

        try:
            print("try ", user_info)
        except Exception as e:
            print("ellol: ", str(e))
            raise serializers.ValidationError("Expired tokens!"
            )
        return attrs