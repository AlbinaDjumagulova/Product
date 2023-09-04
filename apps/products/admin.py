from django.contrib import admin

# Register your models here.


from django.contrib import admin
from apps.products.models import Product

admin.site.register(Product)
