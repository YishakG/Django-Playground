JWT => JSON Web Token
stateless authentication mechanism
User logs in once 
Server gives back a signed token
Client stores token
Client sends token with every request
Server verifies token -> no DB session lookup


2 Tokens
    Access Token
        short lived
        used on every request
    Refresh Token
        long lived
        get new access token

AUTHENTICATION FLOW
User login -> Server validates credentials -> Server sends Access and Refresh token -> Client stores tokens -> client sends access token in headers -> server verifies signature -> allow request

Steps to add
1. pip install djangorestframework
   pip install djangorestframework-simplejwt
2. in settings.py
AUTH_USER_MODEL = "jwt_authentication.User"

INSTALLED_APPS = [
    ...,
    'jwt_authentication',
    'rest_framework',
    "rest_framework_simplejwt.token_blacklist"     # ← enables logout (blacklisting)
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

3. In urls.py
   from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

now you have 
POST /api/token/
POST /api/token/refresh/
 


