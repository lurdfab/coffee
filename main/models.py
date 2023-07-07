from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppInfo(models.Model):
    appname = models.CharField(max_length=30)
    logo  =  models.ImageField(upload_to='logo')
    banner = models.ImageField(upload_to='banner')
    copyright = models.IntegerField()

    def __str__(self):
        return self.appname
    
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    frontpix = models.ImageField(upload_to='frontpix')
    backpix = models.ImageField(upload_to='backpix')

    def __str__(self):
        return self.title
    
class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    old_price =  models.FloatField()
    new_price = models.FloatField()
    pix = models.ImageField(upload_to='pix')
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    brand = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    pimg = models.ImageField(upload_to='pimg')
    old_price = models.FloatField()
    new_price = models.FloatField()
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

class Reviews(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

