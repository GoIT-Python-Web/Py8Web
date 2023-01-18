import sys

import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5671, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='Hello')

    def my_callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='Hello', on_message_callback=my_callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Good buy!')
        sys.exit(0)
