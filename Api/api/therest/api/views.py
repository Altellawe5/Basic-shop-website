from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Category, PriceType, Product, Order, OrderLine
from .serializers import CustomerSerializer, CategorySerializer, PriceTypeSerializer, ProductSerializer, OrderSerializer, OrderLineSerializer
from django.shortcuts import get_object_or_404


# Categories API endpoints

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)




@api_view(['PUT'])
def update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Price Types API endpoints

@api_view(['POST'])
def create_price_type(request):
    serializer = PriceTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_price_type(request, pk):
    try:
        price_type = PriceType.objects.get(pk=pk)
    except PriceType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PriceTypeSerializer(price_type)
    return Response(serializer.data)


@api_view(['PUT'])
def update_price_type(request, pk):
    try:
        price_type = PriceType.objects.get(pk=pk)
    except PriceType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PriceTypeSerializer(price_type, data=request.data)



@api_view(['GET'])
def products_by_category(request, category_id):
    try:
        products = Product.objects.filter(category=category_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '')
    if not query:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    products = Product.objects.filter(name__icontains=query)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from .serializers import CustomerSerializer
# from django.views.decorators.csrf import csrf_exempt

# @api_view(['POST'])
# @csrf_exempt
# @permission_classes([AllowAny])
# def signup(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         user = User.objects.create_user(
#             username=serializer.validated_data['username'],
#             email=serializer.validated_data['email'],
#             password=serializer.validated_data['password']
#         )
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @csrf_exempt
# @permission_classes([AllowAny])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return Response({'detail': 'Authentication succeeded'}, status=status.HTTP_200_OK)
#     return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
