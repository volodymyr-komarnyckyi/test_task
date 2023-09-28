from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic
from spend.serializers import SpendSerializer, SpendRetrieveSerializer


class SpendStatisticsView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("name", "date").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversions=Sum("conversion"),
            total_revenue=Sum("revenuestatistic__revenue"),
        )

        truncated_data = []
        for item in queryset:
            item["date"] = item["date"].strftime("%Y-%m-%d")
            truncated_data.append(item)

        serializer = SpendRetrieveSerializer(truncated_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SpendSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
