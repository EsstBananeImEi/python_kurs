from argparse import ArgumentParser
from functools import reduce
import json
import zmq.asyncio
from random import randint
import asyncio
import sys
import zmq

""" Multi Subscriber """

context = zmq.asyncio.Context()
socket = context.socket(zmq.SUB)


async def run(ports, topic):
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)
    print(f"Subscriber Connected to Servers:")
    for port in ports:
        con_str = f'tcp://127.0.0.1:{port}'
        socket.connect(con_str)
        print(con_str)

    while True:
        _, zmq_message = await socket.recv_multipart()
        print(json.loads(zmq_message))


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--ports", nargs="+", default=["5556"])
        parser.add_argument("-t", "--topic", type=str, default="10001")
        ports = parser.parse_args().ports
        topic = parser.parse_args().topic
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(ports, topic))
    except KeyboardInterrupt:
        exit()
