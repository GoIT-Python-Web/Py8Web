import json
from time import sleep

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5671, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def callback_result(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    sleep(1)
    print('Done!')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback_result)
channel.start_consuming()
