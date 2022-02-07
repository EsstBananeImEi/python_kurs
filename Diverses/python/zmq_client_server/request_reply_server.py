from argparse import ArgumentParser
from random import randint
import zmq.asyncio
import zmq
import asyncio
import time

context = zmq.asyncio.Context()
socket = context.socket(zmq.REP)


async def run(port):
    server_id = randint(1, 2000)
    print(f"Server: {server_id}, Connected to tcp://127.0.0.1:{port}")
    socket.bind(f'tcp://127.0.0.1:{port}')

    while True:
        message = await socket.recv_json()
        print(f"Received request: {message}")
        response_message = {'server': server_id,
                            'zmq_message_type': 'response',
                            'message_recieved': message is not None,
                            'data': message}
        await send_response(response_message)


async def send_response(response_message):
    print(f"Sending Response...")
    time.sleep(1)
    await socket.send_json(response_message)


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--port", type=str, default="5556")
        port = parser.parse_args().port
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(port))

    except KeyboardInterrupt:
        exit()
