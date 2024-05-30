from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import SolicitudSerializer
from producer import brokerSol
from .logic.logic_solicitudes import getSolicitudes, createSolicitud
from SolicitudesApplication.auth0backend import getRole
from django.contrib.auth.decorators import login_required


@login_required
@api_view(['GET'])
def solicitudesList(request):
    role = getRole(request)
    if role == "Gerencia":
        if request.method == 'GET':
            try:
                solicitudes = getSolicitudes()
                serializer = SolicitudSerializer(solicitudes, many = True)
                return Response(serializer.data)
            except Exception:
                return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@login_required           
@api_view(['POST'])
def postSolicitud(request):
    role = getRole(request)
    if role == "Cliente" or role == "Supervisor":
        if request.method == 'POST':
            try:
                solcitud = createSolicitud(request.data)
                brokerSol(solcitud)
                return Response(request.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])      
def healthCheck(request):
    return HttpResponse('ok')
