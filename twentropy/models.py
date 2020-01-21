from django.db import models

# Create your models here.
class Tweet(models.Model):
        id = models.IntegerField(primary_key=True, unique=True )
        created = models.DateTimeField(null=True)
        text = models.CharField(max_length=1000)
        sensitive = models.CharField(max_length=1000, null=True)

class Hacker(models.Model):
        id = models.AutoField(primary_key=True, unique=True )
        created = models.DateTimeField(null=True, auto_now=True)
        email = models.CharField(max_length=1000, null=True)
        phone = models.CharField(max_length=1000, null=True)
        name = models.CharField(max_length=1000, null=True)
        text = models.CharField(max_length=1000, null=True)
