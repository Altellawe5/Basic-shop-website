from rest_framework import serializers
from .models import Customer, Category, PriceType, Product, Order, OrderLine


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    o_customer = serializers.ReadOnlyField(source='category.username')
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total', 'is_paid', 'is_active', 'o_customer']


class OrderLineSerializer(serializers.ModelSerializer):
    ol_product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderLine
        fields = ['id', 'quantity', 'price', 'is_active', 'ol_product']
