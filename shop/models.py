from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from config import settings

# Create your models here.


class CustomUser(AbstractUser):
    phone_num = models.PositiveIntegerField(blank=True,null=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)

    def __str__(self):
        return self.username

class Products(models.Model):
    pr_name = models.CharField(max_length=250,verbose_name='Название товара:')
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE,verbose_name='Брэнд:')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Категория:')
    descrip = models.TextField(verbose_name='Описание продукта:')
    main_image = models.ImageField(upload_to='products/',verbose_name='Главное изображение:')
    image_1 = models.ImageField(upload_to='products/',
                                blank=True,null=True,verbose_name='Изображение 1')
    image_2 = models.ImageField(upload_to='products/',
                                blank=True,null=True,verbose_name='Изображение 2')
    image_3 = models.ImageField(upload_to='products/',
                                blank=True,null=True,verbose_name='Изображение 3')
    price = models.PositiveIntegerField(verbose_name='Цена продукта:')
    available = models.BooleanField(default=True,verbose_name='В наличии')

    def __str__(self):
        return f'{self.pr_name} {self.brand}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Brand(models.Model):
    brand_name = models.CharField(max_length=250,verbose_name='Название брэнда')
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.brand_name
    
    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

class Category(models.Model):
    category_name = models.CharField(max_length=250,verbose_name='Название категории:')
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Comment(models.Model):
    comment_text = models.TextField()
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания:'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор коммента:'

    )
    def __str__(self):
        return f'{self.product.pr_name} - {self.comment_text[:20]}...'