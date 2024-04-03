from solicitudes.models import Solicitud
def getSolicitudes():
    queryset = Solicitud.objects.all().order_by('status')
    return (queryset)

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
        