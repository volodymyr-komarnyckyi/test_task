from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RevenueStatistic
from .serializers import RevenueRetrieveSerializer, RevenueSerializer


class RevenueStatisticsView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversions=Sum("spend__conversion"),
        )

        truncated_data = []
        for item in queryset:
            item["date"] = item["date"].strftime("%Y-%m-%d")
            truncated_data.append(item)

        serializer = RevenueRetrieveSerializer(truncated_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RevenueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
