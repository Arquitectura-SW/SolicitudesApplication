from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import SolicitudSerializer
from producer import log
from .logic.logic_solicitudes import getSolicitudes, createSolicitud

@api_view(['GET'])
def solicitudesList(request):
    if request.method == 'GET':
        try:
            solicitudes = getSolicitudes()
            serializer = SolicitudSerializer(solicitudes, many = True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['POST'])
def postSolicitud(request):
    if request.method == 'POST':
        try:
            print(request.data)
            print(request.data['user'])
            createSolicitud(request.data)
            log(document=request.data['user'], level='INFO', message='Solicitud creada exitosamente')
            return Response(status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])      
def healthCheck(request):
    return HttpResponse('ok')
