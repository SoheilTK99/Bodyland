from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):

    PRODUCT_CATEGOREY_TYPE = (

        ('tools' , 'ابزار'),
        ('clothes' , 'پوشاک'),
        ('Supplement' , 'دارو و مکمل'),
        ('other' , 'لوازم جانبی'),
        
    )

    EXIST_TYPE = (
        ('in stock' , 'موجود'),
        ('out of stock' , 'ناموجود'),
    )


    product_name = models.CharField((" نام محصول "),max_length=30,null=True)
    product_categorey = models.CharField(("دسته بندی"),max_length=20, choices=PRODUCT_CATEGOREY_TYPE, default='tools')
    exist = models.CharField((" موجودیت "),choices=EXIST_TYPE, default='in stock')
    product_discription = models.TextField((" توضیحات "),max_length=200,null=True, blank=True)
    price = models.CharField((" قیمت "),max_length=15, default="0")
    product_rate = models.CharField((" امتیاز "),max_length=15,default="5")
    product_image = models.ImageField((" تصویر محصول "),upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.product_name
    
