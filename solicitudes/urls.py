from django.urls import path
from .views import postSolicitud, solicitudesList, solicitudesListByUserId, solicitudesListByStatus, healthCheck

urlpatterns = [
    path('solicitudes/', solicitudesList),
    path('solicitudes/createSolicitud/', postSolicitud),
    path('solicitudes/<int:document>/', solicitudesListByUserId),
    path('solicitudes/<str:status>/', solicitudesListByStatus),
    path('health-check/', healthCheck),
]
