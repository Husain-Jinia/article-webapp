from django.db import models
from datetime import datetime
from users.models import *
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=256, default="")
    description = RichTextField(blank=True, null=True)
    # description  = models.TextField(default="")
    image = models.ImageField(default = 'default.jpeg', upload_to = 'article_pictures')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, blank=True,related_name='like_articles')
    dislikes = models.ManyToManyField(User, blank=True,related_name='dislike_articles')
    block = models.ManyToManyField(User, blank=True, related_name = 'block_articles' )

    def get_absolute_url(self):
        return reverse("dashboard")
    
    
    def __str__(self):
        return f'{self.title} - {self.author}'
    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
    
    def total_blocks(self):
        return self.dislikes.count()
