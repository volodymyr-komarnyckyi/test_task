from rest_framework import serializers
from .models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"


class RevenueRetrieveSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversions = serializers.IntegerField()
