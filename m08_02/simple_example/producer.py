import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5671, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='Hello')

if __name__ == '__main__':
    channel.basic_publish(exchange='', routing_key='Hello', body='Hello Artur!'.encode())
    print(" [x] Sent 'Hello World!'")
    connection.close()
