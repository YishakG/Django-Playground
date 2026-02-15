from django.contrib import admin

from jwt_authentication.models import User

# Register your models here.
admin.site.register(User)