from django.contrib import admin
from .models import PieChartData

@admin.register(PieChartData)
class PieChartDataAdmin(admin.ModelAdmin):
    list_display = ('category', 'value')
    search_fields = ('category',)