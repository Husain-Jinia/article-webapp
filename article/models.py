from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models
from datetime import datetime
from users.models import *

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=256, default="")
    description  = models.TextField(default="")
    image = models.ImageField(default = 'default.jpeg', upload_to = 'profile_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name='like_articles')

    def total_likes(self):
        return self.likes.count()
