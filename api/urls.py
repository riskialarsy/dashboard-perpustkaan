from django.urls import path
from .views import PieChartDataView

urlpatterns = [
    path('pie-chart-data/', PieChartDataView.as_view(), name='pie-chart-data'),
]