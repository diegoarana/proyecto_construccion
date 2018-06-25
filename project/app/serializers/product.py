from app.models import Product
from rest_framework import serializers

class Product(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product', 'image')