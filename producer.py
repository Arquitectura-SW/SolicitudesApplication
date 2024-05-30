from datetime import datetime, timezone
import pika
from sys import path
from os import environ
import django
import json


rabbit_host = '10.128.0.14'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('SolicitudesApplication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolicitudesApplication.settings')
django.setup()


def log(document: int, level: str, message: str):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='topic')
        timestamp = datetime.now(timezone.utc).isoformat()
        for topic in topics:
            payload = {
                'level': level,
                'message': message,
                'user': document,
                'timestamp': timestamp
            }
            print(f"{level} - {message} - {document} - {timestamp}")
            channel.basic_publish(exchange=exchange, routing_key=topic, body=json.dumps(payload))
        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")

            
        
        
        

