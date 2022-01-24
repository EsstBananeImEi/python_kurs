from argparse import ArgumentParser
import json
import zmq.asyncio
from random import randint
import asyncio
import sys
import zmq

""" Subscriber """

context = zmq.asyncio.Context()
socket = context.socket(zmq.SUB)


async def run(port, topic):
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)
    socket.connect(f'tcp://127.0.0.1:5556')
    print(f"Subscriber Connected to Server tcp://127.0.0.1:{port}")

    while True:
        _, zmq_message = await socket.recv_multipart()
        print(json.loads(zmq_message))


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--port", type=str, default="5556")
        parser.add_argument("-t", "--topic", type=str, default="10001")
        port = parser.parse_args().port
        topic = parser.parse_args().topic
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(port, topic))
    except KeyboardInterrupt:
        exit()
