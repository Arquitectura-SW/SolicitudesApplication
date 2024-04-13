from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import SolicitudSerializer
from .logic.logic_solicitudes import getSolicitudes, createSolicitud, getSolicitudesByUserId, getSolicitudByStatus

@api_view(['GET'])
def solicitudesList(request):
    if request.method == 'GET':
        try:
            solicitudes = getSolicitudes()
            serializer = SolicitudSerializer(solicitudes, many = True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def solicitudesListByUserId(request, document):
    if request.method == 'GET':
        try:
            solicitudes = getSolicitudesByUserId(document)
            serializer = SolicitudSerializer(solicitudes, many = True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def solicitudesListByStatus(request, status):
    if request.method == 'GET':
        try:
            solicitudes = getSolicitudByStatus(status)
            serializer = SolicitudSerializer(solicitudes, many = True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)
              
@api_view(['POST'])
def postSolicitud(request):
    if request.method == 'POST':
        try:
            solcitud = createSolicitud(request.data)
            serializer = SolicitudSerializer(solcitud)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"error": "The Solicitudes wasn't created."}, status=status.HTTP_400_BAD_REQUEST)
        
def healthCheck(request):
    return HttpResponse('ok')
