from solicitudes.models import Solicitud
from clientes.models import Cliente

def getSolicitudes():
    return Solicitud.objects.all().order_by('status')

def createSolicitud(data):
    try:
        user_id = data.get('user')
        cliente = Cliente.objects.get(document=user_id)
        data['user'] = cliente
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
        
def getSolicitudesByUserId(document):
    try:
        if Cliente.objects.get(document=document):
            return Solicitud.objects.filter(user=Cliente.objects.get(document=document))
    except:
        raise Exception({'error': 'Cliente no tiene solicitudes'}, 404)
    
def getSolicitudByStatus(statu):
    try:
        return Solicitud.objects.filter(status=statu)
    except:
        raise Exception({"error": "Solicitudes not found"}, 404)