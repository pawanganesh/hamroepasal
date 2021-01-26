from django.contrib import admin

from .models import Brand, Category, SubCategory, Product

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
