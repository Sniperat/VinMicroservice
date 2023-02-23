from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DetailSerializer
from .utils import get_detail_from_vin


class VinRetrieveApiView(APIView):

    @staticmethod
    def get(request):
        vin_id = request.GET.get('vinId', False)
        if vin_id and len(vin_id) == 17:
            data = get_detail_from_vin(vin_id)
            if data:
                serializer = DetailSerializer(data)
                return Response(data={'status': 'success', 'data': serializer.data})
        return Response(data={'status': 'failed', 'data': 'Vin id is not correct'})
