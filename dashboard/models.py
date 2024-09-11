from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Electronics', 'Electronics'),
    ('Clothing', 'Clothing'),
    ('Books', 'Books'),
    ('Grocery', 'Grocery'),
    ('Furniture', 'Furniture'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    total = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product.name} Ordered by {self.staff.username}'

class Meta:
    verbose_name_plural = 'Staff order'

