from django.db import models

# Create your models here.
from datetime import date
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from article.models import *
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpeg', upload_to = 'profile_pics')
    phone_number = models.CharField(max_length=256,blank=True,default="",null=True)
    category = models.ManyToManyField(Category,related_name='profile')
    dob = models.DateField(default=date.today,blank=True,null=True)
    def __str__(self):
        return f'{self.user.username} Profile'