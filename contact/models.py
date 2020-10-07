from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    email = models.EmailField(max_length=50,blank=False,default='')
    phone = models.CharField(max_length=10,blank=True,default='')
    Desc = models.CharField(max_length=200,blank=False,default='')
    
    def __str__(self):
        return self.name