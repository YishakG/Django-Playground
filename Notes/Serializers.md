Serializers
translate python object <==> JSON(other content types)

1. model instances => JSON
2. JSON/Request Data => Python Object
3. handles validation
   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]
maps fields from your model(User) into the serializers
Automatically handles validation (EmailField checks for valid email)
only the fields will be included in the serialized JSON
Exclude passwords

example 
user opens their app -> /api/profile
user = User.objects.get(id=1)
serializer = UserSerializer(user)
serializer.data 


<!-- Token pair Seralizer -->
validate login credentials and issues JWTs
pair =>access token and refresh token
standard login seralizer for JWT

1. Client sends JSON
2. {
    'username' : 'yeab',
    'password' : 'password'
   }
3. check if username/password are correct
   if valid creates pair of JWTs
    {
        'refresh' :
        'access' :
    }
4. Default JWT payload: created by TokenObtain Pair Seralizer
    {
  "token_type": "access",
  "exp": 1700000000,   // expiration timestamp
  "jti": "abc123",     // unique token ID
  "user_id": 1          // user’s database ID
}
5. Default seralizer doesnot include infor like usernae or email