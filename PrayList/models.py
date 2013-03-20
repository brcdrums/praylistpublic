from django.db import models
import datetime
from django.contrib.auth.models import User

class Group(models.Model):
    groupname = models.CharField(max_length=30)
    privacy = models.BooleanField()
    users_favorited = models.ManyToManyField(User)

class Prayer(models.Model):
    number = 1
    poster = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    subject = models.CharField(max_length=100)
    prayer = models.CharField(max_length=2000)
    prayerscore = models.IntegerField()
    prayed_users = models.ManyToManyField(User)
    hotness = models.IntegerField()
    group = models.ManyToManyField(Group)

