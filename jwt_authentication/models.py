# Gives access to Django’s database field types (CharField, EmailField, etc).
from django.db import models
# AbstractUser: base class already contains username,password,email,first_name,last_name,groups & permissions,authentication logic
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User model that inherits everything from Django’s default user model.
class User(AbstractUser):
    # create an email column and must be unique
    # default in not unique so created to override
    email = models.EmailField(unique=True)
    # main identifier for authentications
    # if you want email login change to email. the default is user name
    # USERNAME_FIELD = "email"
    # fields needed when creating a super user
    # REQUIRED_FIELDS = ["email"] This will ask for email when creating a super user

    def __str__(self):
        return self.username
