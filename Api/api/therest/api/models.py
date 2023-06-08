from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField()

class Category(models.Model):
    name = models.TextField()

class PriceType(models.Model):
    name = models.TextField()

class Product(models.Model):
    name = models.TextField()
    brand = models.TextField()
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    nutriscore = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='p_category', on_delete=models.CASCADE)
    ptype = models.ForeignKey(PriceType, related_name='p_ptype', on_delete=models.CASCADE)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    is_paid = models.BooleanField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Customer, related_name='o_customer', on_delete=models.CASCADE)


class OrderLine(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    is_active = models.BooleanField()
    product = models.ForeignKey(Product, related_name='ol_product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='ol_order', on_delete=models.CASCADE)



