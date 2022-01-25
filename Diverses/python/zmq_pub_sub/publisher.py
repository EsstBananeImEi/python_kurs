import zmq.asyncio
import asyncio
import zmq
import random
import time
from argparse import ArgumentParser


""" Publisher """

context = zmq.asyncio.Context()
socket = context.socket(zmq.PUB)


async def run(port):
    socket.bind(f'tcp://127.0.0.1:{port}')
    print(f"Server is ready listening on port {port}")
    input("Press any key to start sending jobs!")
    await send(port)


async def send(port):
    print("About to send jobs!")

    for message_number in range(1, 100):
        topic = random.randrange(9999, 10002)
        messagedata = random.randrange(-20, 60)
        json_data = {'topic': topic, 'port': port, 'data': messagedata,
                     'message_number': message_number}
        await socket.send_string(str(topic), flags=zmq.SNDMORE)
        await socket.send_json(json_data)
        print(json_data)
        time.sleep(0.2)

if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--port", type=str, default="5556")
        port = parser.parse_args().port
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(port))

    except KeyboardInterrupt:
        exit()
