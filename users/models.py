from contextlib import nullcontext
from distutils.command.upload import upload
from doctest import BLANKLINE_MARKER
import email
from pickle import TRUE
from unicodedata import name
import uuid
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username =  models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=250)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/default-profile.png')
    github = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

class Interests(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=TRUE, blank=TRUE)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
