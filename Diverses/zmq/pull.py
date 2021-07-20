""" Worker """
import asyncio

import zmq.asyncio

context = zmq.asyncio.Context()
socket = context.socket(zmq.PULL)


async def run():
    socket.connect('tcp://127.0.0.1:7000')
    print("Connected to Server")

    while True:
        message = await socket.recv_string()
        print(message)


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
    except KeyboardInterrupt:
        exit()
