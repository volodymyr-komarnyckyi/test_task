from rest_framework import serializers

from spend.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"


class SpendRetrieveSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversions = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
