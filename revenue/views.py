from django.db.models import Sum, OuterRef, Subquery
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from spend.models import SpendStatistic
from .models import RevenueStatistic
from .serializers import RevenueRetrieveSerializer, RevenueSerializer


class RevenueStatisticsView(APIView):
    def get(self, request):
        spend_subquery = SpendStatistic.objects.filter(revenuestatistic=OuterRef('pk')).values('revenuestatistic')

        total_spend_subquery = Subquery(
            SpendStatistic.objects.filter(revenuestatistic=OuterRef("pk"))
            .values("revenuestatistic")
            .annotate(total=Sum("spend"))
            .values("total")[:1]
        )

        total_impressions_subquery = Subquery(
            SpendStatistic.objects.filter(revenuestatistic=OuterRef("pk"))
            .values("revenuestatistic")
            .annotate(total=Sum("impressions"))
            .values("total")[:1]
        )

        total_clicks_subquery = Subquery(
            SpendStatistic.objects.filter(revenuestatistic=OuterRef("pk"))
            .values("revenuestatistic")
            .annotate(total=Sum("clicks"))
            .values("total")[:1]
        )

        total_conversions_subquery = Subquery(
            SpendStatistic.objects.filter(revenuestatistic=OuterRef("pk"))
            .values("revenuestatistic")
            .annotate(total=Sum("conversion"))
            .values("total")[:1]
        )

        queryset = RevenueStatistic.objects.annotate(
            total_revenue=Sum("revenue"),
            total_spend=total_spend_subquery,
            total_impressions=total_impressions_subquery,
            total_clicks=total_clicks_subquery,
            total_conversions=total_conversions_subquery,
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
