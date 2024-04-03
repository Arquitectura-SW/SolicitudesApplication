from datetime import datetime
import time
import pika
import json

from random import choice, randint, uniform

rabbit_host = '10.128.0.5'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='topic')

print(' [*] Waiting for logs. To exit press CTRL+C')

while True:
    for topic in topics:
        status = choice(['Aprobado', 'Rechazado','Pendiente'])
        user_id = randint(-9999999, 99999999)
        creationDate = datetime.now().isoformat()
        payload = {'user_id': user_id, 'status': status, 'creationDate': creationDate, 'topic': topic}
        message = json.dumps(payload)
        channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
        print("Topic: %r, Status: %r, UserId: %r, CreationDate: %r" % (topic, status, user_id, creationDate))
        time.sleep(1)
connection.close()
        
        
        
        

