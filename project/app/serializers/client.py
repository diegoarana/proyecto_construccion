from app.models import Client
from rest_framework import serializers

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'last_name', 'email', 'address', 'location', 'phone')