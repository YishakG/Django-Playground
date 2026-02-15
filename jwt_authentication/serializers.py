from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# dynamically gets the custom User model(whatever you set in AUTH_USER_MODEL)
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # passwords can be sent by client but won't be returned in API responses
    # dont expose hashed passwords in JSON
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","username","email","password"]
    # cleaned and validated data from API request
    def create(self, validated_data):
        # Django's built-in secure method for creating a user
        # automatically hashes the password
        # save user to db
        # User.objects.create() store passwords in plain texts
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
#  Simplified serializer for sending user data back
# Dont include password(safe for API responses)  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]


# TokenObtainPairSerializer handles JWT token creation for login
# by default it creates access and refress tooken containing only the user_id
# notice below it doesnt include username or email
# {
#   "token_type": "access",
#   "exp": 1700000000,
#   "jti": "abc123",
#   "user_id": 1
# }
class CustomTokenSerializer(TokenObtainPairSerializer):
    # Called whenever a token is created
    # user is the user instance trying to login
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        # add the username and email to the token payload
        token["username"] = user.username
        token["email"] = user.email
        # return the modified token
        # {
        #     "token_type": "access",
        #     "exp": 1700000000,
        #     "jti": "abc123",
        #     "user_id": 1,
        #     "username": "yeab",
        #     "email": "yeab@example.com"
        # }
        return token


