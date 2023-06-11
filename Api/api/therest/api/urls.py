from . import views
from .views import  search_products, products_by_category, all_products, get_product, get_categories, get_category

from django.urls import path
urlpatterns = [

    # path('customers/<int:pk>/', get_customer, name='get-customer'),
    path('products/category/<int:category_id>/', products_by_category),
    path('products/', all_products),
    path('products/search/', search_products),
    path('products/<int:pk>/', get_product),
    path('categories/', get_categories),
    path('category/<int:pk>', get_category)

]
