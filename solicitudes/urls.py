from django.urls import path
from .views import postSolicitud, solicitudesList, healthCheck

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('solicitudes/createSolicitud/', postSolicitud),
    path('/health-check/', healthCheck),
]
