from django.db import models
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag

class Prayer(models.Model):
    number = 1
    poster = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    subject = models.CharField(max_length=100)
    prayer = models.CharField(max_length=2000)
    prayerscore = models.IntegerField()
    prayed_users = models.ManyToManyField(User)
    hotness = models.IntegerField()
    tags = TagField()

    def get_tags(self):
        return Tag.objects.get_for_object(self) 
