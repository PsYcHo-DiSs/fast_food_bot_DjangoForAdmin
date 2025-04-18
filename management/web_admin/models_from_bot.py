# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carts(models.Model):
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_products = models.IntegerField()
    user = models.OneToOneField('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carts'


class Categories(models.Model):
    category_name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'categories'


class FinalCarts(models.Model):
    product_name = models.CharField(max_length=50)
    final_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Carts, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'final_carts'
        unique_together = (('cart', 'product_name'),)


class Products(models.Model):
    product_name = models.CharField(unique=True, max_length=20)
    description = models.CharField()
    image = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    name = models.CharField(max_length=50)
    telegram = models.BigIntegerField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
