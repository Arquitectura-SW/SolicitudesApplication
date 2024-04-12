from django.urls import path
from .views import postSolicitud, solicitudesList, solicitudesListByUserId, solicitudesListByStatus

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('solicitudes/createSolicitud/', postSolicitud),
    path('solicitudes/<int:documento>/', solicitudesListByUserId),
    path('solicitudes/<str:status>/', solicitudesListByStatus)
]
