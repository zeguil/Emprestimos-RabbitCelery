import pika
import time

def wait_for_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            connection.close()
            break
        except pika.exceptions.AMQPConnectionError as error:
            print(f'Falha na conexão com o RabbitMQ: {error}')
            print('Aguardando o RabbitMQ...')
            time.sleep(1)

if __name__ == '__main__':
    wait_for_rabbitmq()
