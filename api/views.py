from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PieChartData
from .serializers import PieChartDataSerializer

class PieChartDataView(APIView):
    def get(self, request):
        data = PieChartData.objects.all()
        serializer = PieChartDataSerializer(data, many=True)
        return Response(serializer.data)