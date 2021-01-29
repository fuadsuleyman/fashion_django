from django.shortcuts import render

# Create your views here.

# all_products, get_product, create_product, update_product, delete_product

from product.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .serializers import ProductPriceUpdateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Products':'/product-list/',
        'Detail View':'/product-detail/<str:pk>/',
        'Create':'/product-create/',
        'Update':'/product-update/<str:pk>/',
        'Delete':'/product-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductPriceUpdateSerializer(instance=product, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Item successfully deleted!')