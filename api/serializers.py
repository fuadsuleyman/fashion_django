from rest_framework import serializers
from product.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductPriceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'price',
        )