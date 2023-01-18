import json
from random import randint
from datetime import datetime

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5671, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_exchange', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_exchange', queue='task_queue')

if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        if count >= 10:
            break

        message = {
            'task_id': count,
            'payload': f'Task result: {randint(1, 500)}',
            'created_at': datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange='task_exchange',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
        print(f"Send message: {message}")

    connection.close()
