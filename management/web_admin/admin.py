from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Users, Carts, FinalCarts,
                     Categories, Products)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telegram', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('phone',)
    readonly_fields = ('id', 'name', 'telegram')
    list_filter = ('id', 'name', 'telegram', 'phone')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    search_fields = ('category_name',)
    readonly_fields = ('id',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description', 'price', 'category_id', 'get_image')
    list_display_links = ('id', 'product_name')
    readonly_fields = ('id', 'category_id', 'get_image')
    search_fields = ('product_name', 'description')
    list_filter = ('product_name', 'category_id',)

    def get_image(self, obj):
        if obj.image:
            print(obj.image.url, '----------------------------')
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />')
        return '-'

    get_image.short_description = 'Превью'


class CartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'total_products', 'user_id')
    list_display_links = ('id', 'user_id')
    readonly_fields = ('id', 'total_price', 'total_products', 'user_id')
    list_filter = ('total_price', 'user_id')


class FinalCartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'final_price', 'quantity', 'cart_id')
    list_display_links = ('id', 'product_name', 'cart_id')
    readonly_fields = ('id', 'product_name', 'final_price', 'quantity', 'cart_id')
    list_filter = ('product_name', 'final_price', 'cart_id')


admin.site.register(Users, UsersAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)

admin.site.register(Carts, CartsAdmin)
admin.site.register(FinalCarts, FinalCartsAdmin)
