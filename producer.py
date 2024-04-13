from datetime import datetime
import time
import pika
from sys import path
from os import environ
import django
import json
from random import choice, randint, uniform

rabbit_host = '10.128.0.53'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('SolicitudesApplication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolicitudesApplication.settings')
django.setup()

from solicitudes.logic.logic_solicitudes import createSolicitud, createSolicitudObject, getSolicitudes
from solicitudes.models import Solicitud


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='topic')

def brokerSol(solicitud:Solicitud):
    print(solicitud)
    for topic in topics:
        print(solicitud.creationDate)
        payload = {'user_id': solicitud.user.document,'status':solicitud.status, 'creationDate': str(solicitud.creationDate)}
        message = json.dumps(payload)
        channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
        print("Topic: %r Status: %r, UserId: %r, CreationDate: %r" % (topic, solicitud.status, solicitud.user.document, solicitud.creationDate))
        time.sleep(1)
connection.close()
        
        
        
        

