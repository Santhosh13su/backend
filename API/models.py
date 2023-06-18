import os.path

from django.db import models

# Create your models here.

def saveImg(request,filename):
    return os.path.join('ProductImages/',filename)

class Products(models.Model):
    ProductName=models.CharField(max_length=50,blank=False,null=False)
    Description=models.TextField(blank=False,null=False)
    Price=models.FloatField(blank=False)
    ProductImage=models.ImageField(upload_to=saveImg)

    def __str__(self):
        return self.ProductName