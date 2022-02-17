from email import message
from email.policy import default
from hashlib import blake2b
from pyexpat import model
from turtle import Turtle
from django.db import models
from users.models import Profile
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import uuid


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    tag_name = models.CharField(max_length=350)

    def __str__(self):
        return self.tag_name

class Research(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    research_title = models.CharField(max_length=256)
    banner_image = models.ImageField(null=True, blank=True, default="default-banner.jpg")
    body = RichTextUploadingField(null=True, blank=True)
    hashes = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.research_title


class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return str(self.message)



