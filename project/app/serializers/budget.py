from app.models import Budget
from rest_framework import serializers

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = ('consultation', 'price')