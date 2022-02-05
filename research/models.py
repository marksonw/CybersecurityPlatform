from email import message
from pyexpat import model
from turtle import Turtle
from django.db import models
import uuid
# Create your models here.

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    tag_name = models.CharField(max_length=350)

    def __str__(self):
        return self.tag_name

class Research(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    research_title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=2500, null=True, blank=True)
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
        return self.research



