from django.db import models

from .web_admin_utils import *


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    telegram = models.BigIntegerField(unique=True, verbose_name='Телеграм id')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Контактный номер')

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class Carts(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Итоговая цена')
    total_products = models.IntegerField(default=0, verbose_name='Количество шт.')
    user = models.OneToOneField(Users, models.DO_NOTHING, db_column='user_id', unique=True)

    class Meta:
        managed = False
        db_table = 'carts'
        verbose_name = 'Временная корзина'
        verbose_name_plural = 'Временные корзины'

    def __str__(self):
        return str(self.id)


class FinalCarts(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50, verbose_name='Название товара')
    final_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Итоговая цена')
    quantity = models.IntegerField(default=0, verbose_name='Количество шт.')
    cart = models.ForeignKey(Carts, models.DO_NOTHING, db_column='cart_id')

    class Meta:
        managed = False
        db_table = 'final_carts'
        unique_together = (('cart', 'product_name'),)
        verbose_name = 'Итоговая корзина'
        verbose_name_plural = 'Итоговые корзины'

    def __str__(self):
        return str(self.id)


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=20, unique=True, verbose_name='Название категории')

    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=20, unique=True, verbose_name='Название товара')
    description = models.TextField(default='', verbose_name='Ингридиенты')
    image = models.ImageField(upload_to=PathAndRename('images/'), verbose_name='Изображение')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category_id')

    class Meta:
        managed = False
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product_name
