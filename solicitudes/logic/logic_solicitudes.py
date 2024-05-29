import json
from solicitudes.models import Solicitud
import requests
from SolicitudesApplication import settings

def check_user(data):
    r = requests.get(settings.PATH_USERS, headers={"Accept": "application/json"})
    response_json = r.json()
    users = response_json['data'] 
    for user in users:
        if data["user"] == user["document"]:
            return True
    return False

def getSolicitudes():
    return Solicitud.objects.all().order_by('status')

def createSolicitud(data):
    try:
        if check_user(data):
            return Solicitud.objects.create(**data)
    except:
        raise Exception({"error": "Client not created"}, 404)

def createSolicitudObject(creationDate, closeDate, status, user):
    solicitud = Solicitud()
    solicitud.creationDate = creationDate
    solicitud.closeDate = closeDate
    solicitud.status = status
    solicitud.user = user
    solicitud.save()
        
