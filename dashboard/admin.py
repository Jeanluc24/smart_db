from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'SmartInventory hub  Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)

