from django.contrib import admin
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('price', 'marja', 'package_code')


admin.site.register(Product, ProductAdmin)
