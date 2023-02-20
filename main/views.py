from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import DetailSerializer
from .functions import get_detail_from_vin


class EndpointView(APIView):
    
    def get(self, request):
        return HttpResponse('<h1>Hello world!</h1>')
        
    @swagger_auto_schema(
        operation_id='get_detail',
        operation_description="Get Details",
        responses={
            '200': DetailSerializer()
        },
        manual_parameters=[
            openapi.Parameter('vin', openapi.IN_QUERY, description="write yout vin id",
                              type=openapi.TYPE_STRING)
        ],
    )
    def post(self, request):
        vin_id = request.GET.get('vin', False)
        if vin_id and len(vin_id) == 17:
            data = get_detail_from_vin(vin_id)
            if data:
                serializer = DetailSerializer(data)
                return Response(data=serializer.data)
        
        return Response(data='vin id is not correct!')

