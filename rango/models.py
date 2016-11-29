from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Notice(models.Model):
    title = models.CharField(max_length=128, unique=True)
    num = models.IntegerField(default=0)
    date = models.CharField(max_length=10, default=0)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    keyword1 = models.CharField(max_length=30,blank=True)
    keyword2 = models.CharField(max_length=30,blank=True)


    def __str__(self):
        return self.user.username

class Compared(models.Model):
    user = models.CharField(max_length=10,null=True)
    title = models.CharField(max_length=30,blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.url