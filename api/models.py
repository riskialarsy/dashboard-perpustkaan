from django.db import models

class PieChartData(models.Model):
    category = models.CharField(max_length=100)
    value = models.FloatField()