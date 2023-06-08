from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import Customer, Category, PriceType, Product, Order, OrderLine

# Register your models here.
admin.site.register(Customer, UserAdmin)
admin.site.register(Category)
admin.site.register(PriceType)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderLine)

