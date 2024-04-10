from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(null=True,max_length=2000)
    description = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

