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
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
socket.connect(f'tcp://127.0.0.1:5556')


async def run(port):
    print(f"Subscriber Connected to Server tcp://127.0.0.1:{port}")

    for _ in range(100):

        topic, zmq_message = await socket.recv_multipart()
        print(json.loads(zmq_message))


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--port", type=str, default="5556")
        port = parser.parse_args().port
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(port))
    except KeyboardInterrupt:
        exit()
