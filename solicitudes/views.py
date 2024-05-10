from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import SolicitudSerializer
from producer import brokerSol
from .logic.logic_solicitudes import getSolicitudes, createSolicitud, getSolicitudesByUserId, getSolicitudByStatus
from SolicitudesApplication.auth0backend import getRole
from django.contrib.auth.decorators import login_required

@login_required
@api_view(['GET'])
def solicitudesList(request):
    if request.method == 'GET':
        role = getRole(request)
        if role == "Gerencia":
            try:
                solicitudes = getSolicitudes()
                serializer = SolicitudSerializer(solicitudes, many = True)
                return Response(serializer.data)
            except Exception:
                return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def solicitudesListByUserId(request, document):
    if request.method == 'GET':
        role = getRole(request)
        if role == "Cliente" or role == "Gerencia" or role == "Supervisor":
            try:
                solicitudes = getSolicitudesByUserId(document)
                serializer = SolicitudSerializer(solicitudes, many = True)
                return Response(serializer.data)
            except Exception:
                return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def solicitudesListByStatus(request, status):
    if request.method == 'GET':
        role = getRole(request)
        if role == "Cliente" or role == "Gerencia" or role == "Supervisor":
            try:
                solicitudes = getSolicitudByStatus(status)
                serializer = SolicitudSerializer(solicitudes, many = True)
                return Response(serializer.data)
            except Exception:
                return Response({"error": "The Solicitudes wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@login_required           
@api_view(['POST'])
def postSolicitud(request):
    if request.method == 'POST':
        role = getRole(request)
        if role == "Cliente" or role == "Supervisor":
            try:
                solcitud = createSolicitud(request.data)
                serializer = SolicitudSerializer(solcitud)
                brokerSol(solcitud)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])      
def healthCheck(request):
    return HttpResponse('ok')
