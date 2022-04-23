from logging import getLogger

import pika

from infra.config import settings

log = getLogger(__name__)


def put(message):
    connection = ___get_connection()
    channel = ___get_channel(connection)

    channel.basic_publish(exchange='', routing_key=settings.URL_QUEUE_NAME, body=message)
    log.debug(f"message {message} sent to {settings.URL_QUEUE_NAME}")
    connection.close()


def consume(processors):
    connection = ___get_connection()
    channel = ___get_channel(connection)

    channel.basic_consume(settings.URL_QUEUE_NAME, processors, auto_ack=True)

    channel.start_consuming()  # start consuming (blocks)
    connection.close()


def ___get_channel(connection):
    channel = connection.channel()
    channel.queue_declare(queue=settings.URL_QUEUE_NAME)
    return channel


def ___get_connection():
    credentials = pika.PlainCredentials(username=settings.QUEUE_USER, password=settings.QUEUE_PASS)
    parameters = pika.ConnectionParameters(settings.QUEUE_HOST, settings.QUEUE_PORT, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    return connection
