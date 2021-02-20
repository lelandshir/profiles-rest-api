from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # the python standard for writing a doc string to explain what the class is and does
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Fields for permission system
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Specify model mgmt, Django needs a custom model mgr so it knows how to create users using the CLI tool
    objects = UserProfileManager() 
    # override name fields and requirements
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    # functions for django to get data
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.first_name, self.last_name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name

    def __str__(self):
        """Return a str representation of user"""
        return self.email