""" Worker """
import asyncio
from random import randint
import zmq.asyncio

context = zmq.asyncio.Context()
worker_receiver = context.socket(zmq.PULL)
worker_sender = context.socket(zmq.PUSH)


async def run():
    worker_receiver.connect('tcp://127.0.0.1:7000')
    worker_sender.connect('tcp://127.0.0.1:7001')

    worker_id = randint(1, 1000)
    print(f"Worker {worker_id} Connected to Server")

    while True:
        zmq_message = await worker_receiver.recv_json()
        zmq_response = {'worker': worker_id,
                        'data': zmq_message.get('number'), 'finished': False}
        if zmq_message.get('number') >= 20000:
            zmq_response['finished'] = True
        worker_sender.send_json(zmq_response)
        print(zmq_response)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
    except KeyboardInterrupt:
        exit()
