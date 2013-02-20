from django.db import models
import datetime

class Prayer(models.Model):
	poster = models.CharField(max_length=30)
	timestamp = datetime.datetime.now()
	subject = models.CharField(max_length=50)
	prayer = models.CharField(max_length=500)

	

