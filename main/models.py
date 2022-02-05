from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models.base import Model
from django.shortcuts import render


class Category(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='categories/')
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    characters = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    count_sold = models.IntegerField(default=0, verbose_name=('count sold'))
    qrcode = models.ImageField(upload_to='product_qrcodes/', blank=True, null=True)



    def __str__(self):
        return self.name
    
    



    
    
class Product_discount(models.Model):
    name = models.CharField(max_length=150)
    characters = models.TextField()
    image = models.ImageField(upload_to='products_discount/')
    category = models.ForeignKey(Category, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    count_sold = models.IntegerField(default=0, verbose_name=('count sold'))


    def __str__(self):
        return self.name






class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    count_sold = models.IntegerField(default=0, verbose_name=('count_sold'))



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()



class Site_logo(models.Model):
    logo = models.ImageField(upload_to='site_logos/')



class Slider_image(models.Model):
    image = models.ImageField(upload_to='slider-images/')
    


class Our_brands(models.Model):
    image = models.ImageField(upload_to='brands')



class Informations(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)
    
    def __str__(self):
        return self.phone_number



