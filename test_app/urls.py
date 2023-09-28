from django.contrib import admin
from django.urls import path

from revenue.views import RevenueStatisticsView
from spend.views import SpendStatisticsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("revenue_statistics/", RevenueStatisticsView.as_view()),
    path("spend_statistics/", SpendStatisticsView.as_view()),
]
