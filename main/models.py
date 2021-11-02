from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models
class Category(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    posted_by=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# news details
class NewsDetail(models.Model):    
    image=models.ImageField(null=False, blank=False)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_posted=models.CharField(max_length=30)    
    description=models.TextField(max_length=1300, null=False, blank=False)
    postedby=models.CharField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')
    

class User(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email =models.CharField(max_length=200,null=True)
    profile= models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    