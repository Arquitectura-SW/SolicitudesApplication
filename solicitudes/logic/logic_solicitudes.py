from solicitudes.models import Solicitud
from clientes.models import Cliente

def getSolicitudes():
    return Solicitud.objects.all().order_by('status')

def createSolicitud(formSolicitud):
    solicitud = formSolicitud.save()
    solicitud.save()

def createSolicitudObject(creationDate, closeDate, status, user):
    solicitud = Solicitud()
    solicitud.creationDate = creationDate
    solicitud.closeDate = closeDate
    solicitud.status = status
    solicitud.user = user
    solicitud.save()
        
def getSolicitudesByUserId(document):
    try:
        if Cliente.objects.get(document=document):
            return Solicitud.objects.filter(user=Cliente.objects.get(document=document))
    except Exception as e:
        return None