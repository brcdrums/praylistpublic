from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Groups(models.Model):
    groupname = models.CharField(max_length=30)
    privacy = models.BooleanField()
    users_favorited = models.ManyToManyField(User, related_name='favorited')
    prayer_count = models.IntegerField(default=0)
    total_hotness = models.IntegerField(default=0)

class Prayer(models.Model):
    number = 1
    poster = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    subject = models.CharField(max_length=100)
    prayer = models.CharField(max_length=2000)
    prayerscore = models.IntegerField()
    prayed_users = models.ManyToManyField(User)
    hotness = models.IntegerField()
    group = models.ForeignKey(Groups)

class SavedPrayerCustom(models.Model):
    timestamp = models.DateTimeField()
    custom_prayer = models.CharField(max_length=50)
    prayed_user = models.ForeignKey(User)

class DailyPrayer(models.Model):
    prayed_user = models.ForeignKey(User)
    prayer_id = models.ForeignKey(Prayer, null=True)
    timestamp = models.DateTimeField()
    saved_prayer_custom = models.ForeignKey(SavedPrayerCustom, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    saved_prayer = models.ManyToManyField(Prayer)

    def __str__(self):  
          return "%s's profile" % self.user  



    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
 
post_save.connect(create_user_profile, sender=User) 
 
User.profile = property(lambda u: u.get_profile() )

