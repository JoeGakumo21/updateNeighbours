from django.db import models
from django.db.models.expressions import F

# Create your models
class Category(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    posted_by=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# news details
class NewsDetails(models.Model):    
    image=models.ImageField(null=False, blank=False)
    Category=models.ForeignKey(Category, on_delete=models.SET_NULL)
    date_posted=models.CharField(max_length=30)    
    description=models.CharField(max_length=1300, null=False, blank=False)
    postedby=models.CharField(max_length=200)