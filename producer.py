from datetime import datetime
import time
import pika
from sys import path
from os import environ
import django
import json
from random import choice, randint, uniform

rabbit_host = '10.128.0.14'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('SolicitudesApplication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolicitudesApplication.settings')
django.setup()

from solicitudes.models import Solicitud

def brokerSol(solicitud:Solicitud):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='topic')

        for topic in topics:
            print(solicitud.creationDate)
            payload = {'user_id': solicitud.user,'status':solicitud.status, 'creationDate': str(solicitud.creationDate)}
            message = json.dumps(payload)
            print("Topic: %r Status: %r, UserId: %r, CreationDate: %r" % (topic, solicitud.status, solicitud.user.document, solicitud.creationDate))
            time.sleep(1)
            channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")

            
        
        
        

