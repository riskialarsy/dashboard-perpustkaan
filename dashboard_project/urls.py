from django.contrib import admin
from django.urls import path, include
from .views import PieChartDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]