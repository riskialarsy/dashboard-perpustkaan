from rest_framework import serializers
from .models import PieChartData

class PieChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieChartData
        fields = ['category', 'value']