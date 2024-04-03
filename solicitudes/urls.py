from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postSolicitud, solicitudesList

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('createSolicitud', csrf_exempt(postSolicitud), name = 'createSolicitud'),
]
