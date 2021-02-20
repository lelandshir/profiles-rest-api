from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, first_name, last_name, password=None):
        """Create and save a new user profile"""
        if not email:
            raise ValueError('Whoa there! You need an email address!')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


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