from django.urls import path
from .views import postSolicitud, solicitudesList, solicitudesListByUserId

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('solicitudes/createSolicitud', postSolicitud),
    path('solicitudes/<int:documento>', solicitudesListByUserId),
]
